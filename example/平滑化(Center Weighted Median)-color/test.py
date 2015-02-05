#conding=UTF-8
from PIL import Image
from PIL import ImageFilter
import time
import math
start_time = time.time()

masksize = 3 
Weight = 4

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return int(sortedLst[index])
    else:
        return int((sortedLst[index] + sortedLst[index + 1])/2.0)


for name in range(3,6):
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

    #Smothing(Center Weighted Median)
    for x in range(width-masksize+1):
        for y in range(height-masksize+1):
            meancolor = (0,0,0)

            tmp_r = []
            tmp_g = []
            tmp_b = []
            for i in range(x,masksize+x):
                for j in range(y,masksize+y):
                    (r,g,b) = pix[i,j]
                    w = 1
                    if i==x+1 and j==y+1:
                        w=Weight
                    
                    tmp_r+=[r]*w
                    tmp_g+=[g]*w
                    tmp_b+=[b]*w

            pix_r[x+1,y+1] = (median(tmp_r),median(tmp_g),median(tmp_b))

    #Output
    result_img.save(str(name)+"_output.jpg", quality=100)

print("--- "+ str(time.time() - start_time)+ " seconds ---")

