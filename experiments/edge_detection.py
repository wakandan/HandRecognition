__author__ = 'akai'

import Image
import os
import sys
from cv2 import cv

def analyzeImage(f,name):


    im=Image.open(f)
    try:
        if(im.size[0]==1 or im.size[1]==1):
            return
        print (name+' : '+str(im.size[0])+','+ str(im.size[1]))
        le=1
        if(type(im.getpixel((0,0)))==type((1,2))):
            le=len(im.getpixel((0,0)))
        gray = cv.CreateImage (cv.Size (im.size[0], im.size[1]), 8, 1)
        edge1 = cv.CreateImage (cv.Size (im.size[0], im.size[1]), 32, 1)
        edge2 = cv.CreateImage (cv.Size (im.size[0], im.size[1]), 8, 1)
        edge3 = cv.CreateImage (cv.Size (im.size[0], im.size[1]), 32, 3)

        for h in range(im.size[1]):
            for w in range(im.size[0]):
                p=im.getpixel((w,h))
                if(type(p)==type(1)):
                    gray[h][w] = im.getpixel((w,h))
                else:
                    gray[h][w] = im.getpixel((w,h))[0]

        cv.CornerHarris(gray,edge1,5,5,0.1)
        cv.Canny(gray,edge2,20,100)

        cv.NamedWindow("win")
        cv.ShowImage("win", gray)
        cv.NamedWindow("win2")
        cv.ShowImage("win2", edge1)
        cv.NamedWindow("win3")
        cv.ShowImage("win3", edge2)

        cv.WaitKey()

        f.close()
    except Exception,e:
        print e
        print 'ERROR: problem handling '+ name


image_name = 'E:/doc/programming/oss/HandRecognition/experiments/runtime/hand_color.jpg'
f = open(image_name,'r')
analyzeImage(f, image_name)
