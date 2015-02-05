# -*- coding: utf-8 -*-
import Image,ImageEnhance,ImageFilter,ImageDraw
import binarization
import time


'''大津法由大津於1979年提出，對圖像Image，記t為前景與背景的分割閾值，
前景點數佔圖像比例為w0，
平均灰度為u0；
背景點數佔圖像比例為w1，
平均灰度為u1。
圖像的總平均灰度為：u=w0*u0+w1*u1。
從最小灰度值到最大灰度值遍歷t，
當t使得值g=w0*(u0-u)2+w1* (u1-u)2
最大時t即為分割的最佳閾值。
 直接應用大津法計算量較大，因此我們在實現時採用了等價的公式g=w0*w1*(u0-u1)^2。
'''
def OtsuGrayThreshold(image):
    # 創建Hist
    #image = Image.open("4.f")
    image.convert('L')
    hist = image.histogram()
    print  len(hist)
    #print hist


    # 計算總亮度
    totalH = 0
    for h in range(0,256):
        v =hist[h]
        if v == 0 : continue
        totalH += v*h
        #print h,totalH,v*h
        

    width  = image.size[0]
    height = image.size[1]
    total  = width*height #總像素
    print width
    print height
    
    print "總像素:%d;總亮度:%d平均亮度:%0.2f"%(total,totalH,totalH/total)
    
    v = 0

    gMax = 0.0 
    tBest = 0 #最佳閾值
    
    # temp
    n0Acc = 0.0
    n1Acc = 0.0
    n0H   = 0.0
    n1H   = 0.0
    for t in range(1,255):
        v = hist[t-1]
        if v == 0: continue
        
        n0Acc += v              #灰度 < t 的像素的 數目
        n0H += (t-1)*v          #灰度 < t 的像素的 總亮度
        
        n1Acc = total - n0Acc   #灰度 >=t 的像素的 數目
        n1H = totalH - n0H      #灰度 >=t 的像素的 總亮度

        if n0Acc > 0 and n1Acc > 0:
            u0 = n0H/n0Acc      # 灰階 < t 的 平均灰度
            u1 = n1H/n1Acc      # 灰階 >=t 的 平均灰度
            w0 = n0Acc/total    # 灰階 < t 的 像素比例
            w1 = 1.0-w0         # 灰階 >=t 的 像素比例
            uD = u0-u1
            g = w0 * w1 * uD * uD

            if gMax < g:    #找出最大的g
                gMax   = g
                tBest = t
        
#    if debug >0 : print "gMaxValue=%.2f; t = %d ; t_inv = %d"\
#               %(gMax,tIndex,255-tIndex)            
#    print tIndex 
    return tBest

def OtsuGray(image):
    otsuthreshold = OtsuGrayThreshold(image) #取閾值
    bim = binarization.binarization(image, otsuthreshold) #二值化
    return bim
    

if __name__ =='__main__':
    
    for name in range(1,3):
        start_time = time.time()
        img = Image.open(str(name)+".jpg")


        otsu=OtsuGray(img)

        otsu.save(str(name)+"_output.jpg", quality=100)

        print("--- "+ str(time.time() - start_time)+ " seconds ---")
