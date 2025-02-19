# Sentinel-2 L2A Batch Processing for LULC Segmentation

This repository automates the processing of Sentinel-2 L2A `.SAFE.zip` files for Land Use/Land Cover (LULC) segmentation. It extracts, processes, and merges Sentinel-2 bands into a **10-band** GeoTIFF with **10m resolution**, handling multiple tiles and subfolders automatically.

---

## 📌 Features
- ✅ Processes `.SAFE.zip` files inside multiple tile folders (e.g., `T34SEH`, `T35FJ`)
- ✅ Extracts `.SAFE` folders
- ✅ Resamples **20m bands to 10m** using bilinear interpolation
- ✅ Merges 10 bands into a single **multi-band GeoTIFF**
- ✅ Saves output TIFF in the same directory as the original `.SAFE.zip`
- ✅ Deletes extracted `.SAFE` folders after processing to free up space

---

## 📂 Folder Structure (Before & After Processing)

### **Before Processing:**
```plaintext
D:\Datasets\...\
 ├── T34SEH\
 │    ├── M1\  (Contains .SAFE.zip)
 │    ├── M2\  (Contains .SAFE.zip)
 │    ├── M3\  (Contains .SAFE.zip)
 ├── T35FJ\
 │    ├── M1\  (Contains .SAFE.zip)
 │    ├── M2\  (Contains .SAFE.zip)
 │    ├── M3\  (Contains .SAFE.zip)
```

### **After Processing (Extracted Folder is Deleted!):**
```plaintext
D:\Datasets\...\
 ├── T34SEH\
 │    ├── M1\  (Contains final .tif)
 │    ├── M2\  (Contains final .tif)
 │    ├── M3\  (Contains final .tif)
 ├── T35FJ\
 │    ├── M1\  (Contains final .tif)
 │    ├── M2\  (Contains final .tif)
 │    ├── M3\  (Contains final .tif)
```

---

## 🚀 Installation

### **1️⃣ Install GDAL (Required)**
#### Using Conda:
```bash
conda install -c conda-forge gdal
```
#### Using Pip:
```bash
pip install gdal
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/TasosTemenos/Sentinel-2-L2A-to-GeoTIFF.git
cd Sentinel-2-L2A-to-GeoTIFF
```

### **3️⃣ Install Required Python Packages**
```bash
pip install numpy zipfile36
```

---

## ⚡ Usage
### **Run the Script**
```bash
python SAFE2GEOTIFF.py
```

By default, the script processes all `.SAFE.zip` files inside `D:\Datasets\Sentinel2_L2A\` across multiple tiles (`T34SEH`, `T35FJ`, etc.), and their respective subfolders (`M1`, `M2`, `M3`).

---

## 🖼️ Output Details
- **Output Format:** GeoTIFF (`.tif`)
- **Final Bands:**
  - `B02`, `B03`, `B04`, `B05`, `B06`, `B07`, `B08`, `B8A`, `B11`, `B12`
- **Resolution:** All bands resampled to **10m**
- **Data Type:** `UInt16`

---

## ✅ Example Output File
```plaintext
D:\Datasets\Sentinel2_L2A\T34SEH\M1\S2A_MSIL2A_20210508T092031_N0500_R093_T34SEH_20230303T142851_10bands_uint16.tif
```
