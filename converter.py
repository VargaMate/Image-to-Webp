import os
from PIL import Image

source_folder = 'images'
target_folder = 'webp_images'

os.makedirs(target_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, os.path.splitext(filename)[0] + '.webp')
        try:
            with Image.open(source_path) as img:
                img.save(target_path, 'webp')
        except Exception as e:
            print(f'Failed to convert {filename}: {e}')
