#conding=UTF-8
from PIL import Image
from PIL import ImageFilter


def binarization(img, threshold):
    pix = img.load()
    (width, height) = img.size
    
    gray_img = Image.new('L', (width,height))
    pix_gray = gray_img.load()
    
    #print width,height

    for x in range(width):
        for y in range(height):
            (r,g,b) = pix[x,y]
            pix_gray[x,y] = 0.299*r + 0.587*g + 0.114*b
            #binarization
            if pix_gray[x,y] <= threshold:
                pix_gray[x,y] = 0
            else:
                pix_gray[x,y] = 255
    return gray_img



if __name__ =='__main__':
    for name in range(1,3):
        img = Image.open(str(name)+".jpg")
        binarization(img, 128).save(str(name)+"_output.jpg", quality=100)
    
