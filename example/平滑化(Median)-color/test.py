#conding=UTF-8
from PIL import Image
from PIL import ImageFilter
import time
import math
start_time = time.time()

masksize = 3

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    if len(lst) %2 == 0:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0


for name in range(3,4):
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

    #Smothing(Median)
    for x in range(width-masksize+1):
        for y in range(height-masksize+1):
            meancolor = (0,0,0)

            tmp_r = []
            tmp_g = []
            tmp_b = []
            for i in range(x,masksize+x):
                for j in range(y,masksize+y):
                    (r,g,b) = pix[i,j]
                    tmp_r+=[r]
                    tmp_g+=[g]
                    tmp_b+=[b]

            pix_r[x+1,y+1] = (median(tmp_r),median(tmp_g),median(tmp_b))

    #Output
    result_img.save(str(name)+"_output.jpg", quality=100)

print("--- "+ str(time.time() - start_time)+ " seconds ---")

