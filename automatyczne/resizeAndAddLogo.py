#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
#LOGO_FILENAME = 'catlogo.png'
#FILE = 'C:\\Users\\Mat\\Desktop\\suplement do dyplomu oryg'
FILE = "/home/mateusz/Pobrane/IMG_20201123_143550.jpg"

#logoIm = Image.open(LOGO_FILENAME)
#logoWidth, logoHeight = logoIm.size
#os.chdir(FILE)
# os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
#for filename in os.listdir(FILE):
     #print(filename)
#     if not (filename.endswith('.png') or filename.endswith('.jpg')):
#       # or filename == LOGO_FILENAME:
#         continue # skip non-image files and the logo file itself

im = Image.open(FILE)
width, height = im.size

    # Add logo.
    #print('Adding logo to %s...' % (filename))
    #im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    ## Check if image needs to be resized.
    #if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    #    # Calculate the new width and height to resize to.
    #    if width > height:
    #        height = int((SQUARE_FIT_SIZE / width) * height)
    #        width = SQUARE_FIT_SIZE
    #    else:
    #        width = int((SQUARE_FIT_SIZE / height) * width)
    #        height = SQUARE_FIT_SIZE

        # Resize the image.
print('Resizing %s...' % (FILE))
im = im.resize((int(0.4*width), int(0.4*height)))
#im = im.resize((720, 1440))


# Save changes.
im.save(FILE[:-3] + "zmn.jpg")
