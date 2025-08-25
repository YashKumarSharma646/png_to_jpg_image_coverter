# png_to_jpg_image_coverter
# 🖼️ Image Processing Project (Batch Image Converter)

A simple Python project that converts all images in a folder into another format (e.g., JPG → PNG or PNG → JPG).  
It uses the **PIL (Pillow)** library and handles common real-world issues like missing arguments, wrong paths, and transparency in images.

---

## ⚙️ Tech Stack
- **Python 3**
- **PIL (Pillow)**
- **os, sys**

---

## 📂 How to Run

1. Place your input images in a folder (e.g., `pokedex`).
2. Open terminal in the project directory.
3. Run:
   ```bash
   python IPproject.py pokedex newimage
   ```
   - `pokedex` → input folder (must exist)
   - `newimage` → output folder (created automatically if not exists)

---

## 🚨 Errors Faced & Fixes

### 1. IndexError: list index out of range
**Cause:** Did not provide input and output folder arguments.  
**Fix:** Run with both arguments:  
```bash
python IPproject.py pokedex newimage
```

---

### 2. FileNotFoundError: No such file or directory
**Cause:** Path was wrong → `pokedexbulabasour.png` instead of `pokedex/bulabasour.png`.  
**Fix:** Use `os.path.join()` to properly join paths.

---

### 3. KeyError: 'JPG'
**Cause:** Pillow does not recognize `'jpg'`, only `'JPEG'`.  
**Fix:**  
```python
img.save('file.jpg', 'JPEG')
```

---

### 4. OSError: cannot write mode RGBA as JPEG
**Cause:** Some `.png` images had transparency (`RGBA` mode), which JPEG does not support.  
**Fix:** Convert `RGBA` → `RGB` before saving:
```python
if img.mode == "RGBA":
    img = img.convert("RGB")
```

---

## ✅ Final Working Code

```python
import sys
import os
from PIL import Image

# Take input and output folder from command-line arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each file in the input folder
for filename in os.listdir(image_folder):
    file_path = os.path.join(image_folder, filename)
    img = Image.open(file_path)

    # Convert RGBA → RGB if needed (for JPEG compatibility)
    if img.mode == "RGBA":
        img = img.convert("RGB")

    clean_name = os.path.splitext(filename)[0]
    img.save(os.path.join(output_folder, f'{clean_name}.jpg'), 'JPEG')

print("✅ All done! Images converted successfully.")
```

---

## 🌟 Future Improvements
- Allow user to **choose output format** (PNG/JPEG/BMP).  
- Skip non-image files automatically.  
- Add logging & error handling.  
- GUI support for easy use.

---

## 👨‍💻 Author
Yash Kumar Sharma  
Pre-final year Computer Engineering student | Aspiring Data Scientist & Software Engineer
