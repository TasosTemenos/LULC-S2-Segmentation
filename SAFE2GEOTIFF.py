import os
import glob
import zipfile
import shutil
from osgeo import gdal

# --- Define Parent Directory ---
parent_dir = r"D:\Datasets\ESA-LAND\download\training"  # Top-level folder containing all tile folders (T34SEH, T35FJ, etc.)

# --- Find All ZIP Files in Tile Subfolders (M1, M2, M3) ---
zip_files = glob.glob(os.path.join(parent_dir, "*", "M*", "*.SAFE.zip"))

# --- Sentinel-2 Bands (Excluding 60m Bands) ---
BAND_ORDER = ["B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B11", "B12"]  # Correct Order


# --- Function to Find Band Files ---
def get_band_path(safe_folder, band_name):
    """Search for the correct band path inside SAFE."""
    possible_folders = [
        "GRANULE/*/IMG_DATA/R10m",  # 10m bands
        "GRANULE/*/IMG_DATA/R20m"  # 20m bands
    ]

    for folder in possible_folders:
        band_list = glob.glob(os.path.join(safe_folder, folder, f"*_{band_name}_*.jp2"))
        if band_list:  # If files are found, return the first match
            return band_list[0]

    raise FileNotFoundError(f"Band {band_name} not found in {safe_folder}")


# --- Process Each ZIP File ---
for zip_path in zip_files:
    folder_dir = os.path.dirname(zip_path)  # Get the directory (M1, M2, or M3 inside a tile folder)
    extract_folder = os.path.join(folder_dir, "extracted")  # Temporary extraction folder

    # --- Extract ZIP if not already extracted ---
    if not os.path.exists(extract_folder):
        print(f"\n📦 Extracting: {zip_path} ...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        print("✅ Extraction complete!")

    # --- Locate .SAFE Folder ---
    safe_folder = glob.glob(os.path.join(extract_folder, "*.SAFE"))[0]
    safe_name = os.path.basename(safe_folder).replace(".SAFE", "")  # Extract SAFE filename
    output_tiff = os.path.join(folder_dir, f"{safe_name}_10bands_uint16.tif")  # Save TIFF in same folder as ZIP
    print(f"📌 SAFE file extracted to: {safe_folder}")
    print(f"📤 Output TIFF will be saved at: {output_tiff}")

    # --- Resample 20m Bands to 10m ---
    resampled_bands = {}

    # 1️⃣ Process 10m bands (No resampling needed)
    for band_name in BAND_ORDER:
        band_path = get_band_path(safe_folder, band_name)
        resampled_band_path = os.path.join(extract_folder, f"{band_name}_10m.tif")

        if band_name in ["B02", "B03", "B04", "B08"]:  # 10m Bands
            gdal.Translate(resampled_band_path, band_path, format="GTiff")
        else:  # 20m Bands → Resample to 10m
            gdal.Warp(resampled_band_path, band_path, xRes=10, yRes=10, resampleAlg="bilinear", format="GTiff")

        resampled_bands[band_name] = resampled_band_path
        print(f"🟢 Processed {band_name}: {resampled_band_path}")

    # --- Merge All 10 Bands in the Correct Order ---
    print("\n🔹 Merging 10 bands into a single GeoTIFF...")
    sorted_bands = [resampled_bands[b] for b in BAND_ORDER]  # Order bands correctly

    gdal.BuildVRT(os.path.join(extract_folder, "stacked_10bands.vrt"), sorted_bands, separate=True)
    gdal.Translate(output_tiff, os.path.join(extract_folder, "stacked_10bands.vrt"), format="GTiff",
                   outputType=gdal.GDT_UInt16)

    print(f"✅ Final processed image saved at: {output_tiff} (UInt16, 10 bands, 10m resolution)")

    # --- Clean Up: Delete Extracted Folder After Processing ---
    print("\n🗑️ Deleting extracted folder to free up space...")
    shutil.rmtree(extract_folder)
    print("✅ Extraction folder deleted successfully!")

print("\n🚀 All Sentinel-2 .SAFE.zip files in all tiles have been processed successfully!")
