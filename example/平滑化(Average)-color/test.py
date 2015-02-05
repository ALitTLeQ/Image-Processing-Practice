#conding=UTF-8
from PIL import Image
from PIL import ImageFilter


masksize = 3
weightsum = masksize * masksize

for name in range(1,3):
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

    #Smothing(Average)
    for x in range(width-masksize+1):
        for y in range(height-masksize+1):
            meancolor = (0,0,0)
            
            for i in range(x,masksize+x):
                for j in range(y,masksize+y):
                    (r,g,b) = pix[i,j]
                    (rw,gw,bw)=(r/weightsum, g/weightsum ,b/weightsum)
                    meancolor = (meancolor[0]+rw, meancolor[1]+gw, meancolor[2]+bw)
                    
            pix_r[x+1,y+1] = meancolor

    #Output
    result_img.save(str(name)+"_output.jpg", quality=100)



