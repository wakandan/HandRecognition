__author__ = 'akai'


import cv2.cv as cv

capture = cv.CaptureFromCAM(0)
img_size = cv.GetSize(cv.QueryFrame(capture))
source = cv.CreateImage(img_size, 8, 3)
hsv_img = cv.CreateImage(img_size, 8, 3)
hsv_mask = cv.CreateImage(img_size, 8, 1)
hsv_min = cv.Scalar(0, 30, 80, 0)
hsv_max = cv.Scalar(20, 150, 255, 0)

while True:
    src = cv.QueryFrame( capture)
    cv.NamedWindow( "src",1)
    cv.ShowImage( "src", src)

    cv.CvtColor(src, hsv_img, cv.CV_BGR2HSV)
    cv.NamedWindow( "hsv-img",1)
    cv.ShowImage( "hsv-img", hsv_img)

    cv.InRangeS(hsv_img, hsv_min, hsv_max, hsv_mask)

    cv.NamedWindow("hsv-msk",1)
    cv.ShowImage( "hsv-msk", hsv_mask)
#    hsv_mask.origin = 1
    c =cv.WaitKey(10)
    if c == 27: #exit
        break
    elif c==13:
        #save the image to a file
        cv.SaveImage('runtime/image.jpg', src)
        break
