__author__ = 'akai'

from cv2 import cv

_red =  (0, 0, 255, 0);
_green =  (0, 255, 0, 0);
_white = cv.RealScalar (255)
_black = cv.RealScalar (0)
_contour_thickness = 3
levels = 3
def on_trackbar(position):
    '''
    position is the value of the track bar
    '''
    img_result = cv.CreateImage(src_img_size, 8, 1)
    cv.Canny(img_gray, img_result, position, position*2, 3)
    cv.ShowImage("contours", img_result)
    storage = cv.CreateMemStorage()
    contours = cv.FindContours(img_result, storage,  cv.CV_RETR_TREE, cv.CV_CHAIN_APPROX_SIMPLE)
    print contours
    # draw contours in red and green
    cv.DrawContours (img_result, #dest image
        contours, #input contours
        _red, #color of external contour
        _green, #color of internal contour
        levels, #maxlevel of contours to draw
        _contour_thickness,
        cv.CV_AA, #line type
        (0, 0)) #offset
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
