#conding=UTF-8
from PIL import Image
from PIL import ImageFilter


masksize = 3
weightsum = masksize * masksize

for name in range(1,3):
    img = Image.open(str(name)+".jpg")
    pix = img.load()
    (width, height) = img.size

    gray_img = Image.new('L', (width,height))
    pix_gray = gray_img.load()

    print width,height

    #to Gray
    for x in range(width):
        for y in range(height):
            (r,g,b) = pix[x,y]
            pix_gray[x,y] = 0.299*r + 0.587*g + 0.114*b
    gray_img.save(str(name)+"_gray.jpg", quality=100)
    
    #Smothing(Average)
    for x in range(width-2):
        for y in range(height-2):
            meangray = 0
        
            for i in range(x,masksize+x):
                for j in range(y,masksize+y):
                    meangray = meangray + ((float)(pix_gray[i,j] / weightsum))
                    
            pix_gray[x+1,y+1] = meangray

    gray_img.save(str(name)+"_output.jpg", quality=100)



