'''
DESCRIPTION
    This app parses json to data structures

CONFIGURE
    pip install Pillow
    pip install pillow_heif

NOTES
    Created this on my Mac
'''
import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register the HEIF opener with Pillow
register_heif_opener()

# Set the directory containing the HEIC files
directory = '/Users/< mac user >/_apps/python_venv/my_python_apps/heic_to_png/install_pics'

i = 0

# Loop through all files in the directory
for filename in os.listdir(directory):
    i = i+1
    print("\nfor loop" + str(i))
    print ("file name: " + str(filename))
    if filename.endswith(".HEIC"):
        print("found an HEIC")
        # Open the HEIC file
        filepath = os.path.join(directory, filename)
        with Image.open(filepath) as img:
            # Save the image as PNG
            print("saving image")
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_filepath = os.path.join(directory, png_filename)
            img.save(png_filepath)
