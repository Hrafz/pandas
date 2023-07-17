# read an image and change its extension from .jpg to .png
import sys
import os
from PIL import Image
from pathlib import Path

# grab first and second argument
image_folder = Path(os.getcwd()) / "weather.jpg"
output_folder = Path(os.getcwd()) / "weather.png"


img = Image.open(image_folder)

# save to the new folder
img.save(output_folder, 'png')
print('all done!')
