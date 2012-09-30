__author__ = 'akai'

from cv2 import cv

def on_trackbar(position):
    '''
    position is the value of the track bar
    '''

    img_result = cv.CreateImage(src_img_size, 8, 1)
    cv.Canny(img_gray, img_result, position, position*2, 3)
    cv.ShowImage("contours", img_result)

    pass

def on_trackbar_smooth(position):
    cv.Smooth(img_gray, img_gray, smoothtype=cv.CV_BLUR, param1=2*position+1)
    pass

src_file = 'runtime/hand_color.jpg'
src_img = cv.LoadImage(src_file)
src_img_size = cv.GetSize(src_img)
img_gray = cv.CreateImage(src_img_size, 8, 1)
cv.CvtColor(src_img, img_gray, cv.CV_BGR2GRAY)
cv.NamedWindow("converted-image", 1)
cv.ShowImage("converted-image", img_gray)
cv.Smooth(img_gray, img_gray, smoothtype=cv.CV_BLUR)
cv.NamedWindow("contours", 1)
print cv.CreateTrackbar("(pre) smoothness", 'contours', 0, 7, on_trackbar_smooth)
print cv.CreateTrackbar ("canny threshold", "contours", 0, 7, on_trackbar)
cv.ShowImage("contours", img_gray)
cv.WaitKey(0)
