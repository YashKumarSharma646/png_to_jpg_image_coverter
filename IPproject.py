import sys
import os
from PIL import Image

image_folder=sys.argv[1]
output_folder=sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    file_path = os.path.join(image_folder, filename)
    img = Image.open(file_path)

    # Convert RGBA → RGB if needed
    if img.mode == "RGBA":
        img = img.convert("RGB")

    clean_name = os.path.splitext(filename)[0]
    img.save(os.path.join(output_folder, f'{clean_name}.jpg'), 'JPEG')

# for filename in os.listdir(image_folder):
#     file_path = os.path.join(image_folder, filename)  # joins folder + file properly
#     img = Image.open(file_path)
#     clean_name=os.path.splitext(filename)[0]
#     img.save(os.path.join(output_folder, f'{clean_name}.jpg'), 'JPEG')
#     print('all done')