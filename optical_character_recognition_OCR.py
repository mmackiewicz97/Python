#Pillow, tesseract
#sudo apt-get tesseract-ocr
#export TESSDATA_PREFIX=/usr/local/share/

from PIL import Image, ImageFilter
kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()

from PIL import Image
import subprocess
def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
#Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)
#call tesseract to do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "output"])
#Open and read the resulting data file
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()
cleanFile("text_2.png", "text_2_clean.png")
