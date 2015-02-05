#conding=UTF-8
from PIL import Image
from PIL import ImageFilter
import time
import operator
start_time = time.time()

masksize = 3 
Weight = 3

def equalize(h):
    lut = []
    for b in range(0, len(h), 256):
        # step
        step = reduce(operator.add, h[b:b+256]) / 255
        # create table
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + h[i+b]
    return lut



for name in range(1,4):
    img = Image.open(str(name)+".jpg")
    
    pix = img.load()
    (width, height) = img.size

    print width,height

    result_img = img
    pix_r = result_img.load()

    '''
    #to Gray
    gray_img = Image.new('L', (width,height))
    pix_gray = gray_img.load()

    for x in range(width):
        for y in range(height):
            (r,g,b) = pix[x,y]
            pix_gray[x,y] = 0.299*r + 0.587*g + 0.114*b
    gray_img.save(str(name)+"_gray.jpg", quality=100)
    '''

    #Histogram Equalization
    lut = equalize(img.histogram())
    #search table
    result_img = img.point(lut)

    #Output
    result_img.save(str(name)+"_output.jpg", quality=100)

print("--- "+ str(time.time() - start_time)+ " seconds ---")

