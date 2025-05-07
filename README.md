🪨 GROM’S IMAGE CONVERTER – MAKE PICTURE FAST
Me Grom. Me make tool. Tool take old picture rock (.jpg, .png, .bmp...) and make new faster rock (.webp). You want speed? Grom give speed.

🔧 What Grom Tool Do?
Look in images/ cave

Take all good picture rocks

Turn into .webp with magic

Put in webp_images/ cave

📜 Grom Script
python
Copy
Edit
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
🧠 How Grom Use?
Put old pictures in images/ cave

Run script with python

Look in webp_images/ for shiny new rocks

Grom happy, tribe fast

🐗 Grom Say
"Slow picture? Bad. Big picture? Bad. WebP? GOOOOOD."
