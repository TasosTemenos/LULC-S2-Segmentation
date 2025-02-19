# LULC-S2-Segmentation

# Sentinel-2 L2A Batch Processing Script

This project automates the processing of Sentinel-2 L2A `.SAFE.zip` files. It extracts, processes, and merges Sentinel-2 bands into a **10-band** GeoTIFF with **10m resolution**, while handling multiple tiles and subfolders automatically.

---

## 📌 Features
- ✅ Automatically detects and processes `.SAFE.zip` files inside multiple tile folders (e.g., `T34SEH`, `T35FJ`)
- ✅ Extracts `.SAFE` folders
- ✅ Resamples **20m bands to 10m** using bilinear interpolation
- ✅ Merges 10 bands into a single **multi-band GeoTIFF**
- ✅ Saves output TIFF in the same directory as the original `.SAFE.zip`
- ✅ Deletes extracted `.SAFE` folders after processing to free up space

---

## 📂 Folder Structure (Before & After Processing)

### **Before Processing:**
```plaintext
D:\Datasets\ESA-LAND\download\training\
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
D:\Datasets\ESA-LAND\download\training\
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
git clone https://github.com/your-username/sentinel2-processing.git
cd sentinel2-processing
```

### **3️⃣ Install Required Python Packages**
```bash
pip install numpy zipfile36
```

---

## ⚡ Usage
### **Run the Script**
```bash
python process_sentinel2.py
```

By default, the script will process all `.SAFE.zip` files inside `D:\Datasets\ESA-LAND\download\training\` across multiple tiles (`T34SEH`, `T35FJ`, etc.), and their respective subfolders (`M1`, `M2`, `M3`).

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
D:\Datasets\ESA-LAND\download\training\T34SEH\M1\S2A_MSIL2A_20210508T092031_N0500_R093_T34SEH_20230303T142851_10bands_uint16.tif
```

---

## 🛠️ Troubleshooting
**Issue:** `FileNotFoundError: Band BXX not found`
- Solution: Check if the `.SAFE` structure is different. Run:
```bash
python check_sentinel2_structure.py
```

**Issue:** `GDAL missing or not found`
- Solution: Try reinstalling GDAL:
```bash
conda install -c conda-forge gdal
```

---

## 📜 License
This project is licensed under the MIT License.

---

## 📬 Contact
For any issues, feel free to open an **issue** or contact me at **your.email@example.com**.

🚀 **Happy Processing!**

