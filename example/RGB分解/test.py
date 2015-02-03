#conding=UTF-8
from PIL import Image
from PIL import ImageFilter

file = 1

img = Image.open("1.jpg")

img = img.convert('RGB')

pix = img.load()

(width, height) = img.size

print width,height

for x in range(width):
    for y in range(height):
        (r,g,b) = pix[x,y]
        pix[x,y] = (b,r,g)



img.save("1_output.jpg", quality=100)



