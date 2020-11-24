from PIL import Image
#import cv2 as cv
import os

def PNG_JPG(PngPath):
    
    infile = PngPath
    outfile = "../" + os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)
        else:
            img.convert('RGB').save(outfile, quality=80)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)


path = './data-20191126-qipange'
count = 1
for file in os.listdir(path):
    PngPath = os.path.join(path,file)
    PNG_JPG(PngPath)
    count+=1