__author__ = 'akai'
from cv2 import cv

_red = (0, 0, 255, 0);
_green = (0, 255, 0, 0);
_white = cv.RealScalar(255)
_black = cv.RealScalar(0)
_contour_thickness = 1

image = cv.LoadImage('runtime/image.jpg')
cv.NamedWindow("loaded-image", 1)
img_size = cv.GetSize(image)
cv.ShowImage("loaded-image", image)
# create the storage area
storage = cv.CreateMemStorage(0)
img_grayscale = cv.CreateImage(img_size, 8, 1)
cv.CvtColor(image, img_grayscale, cv.CV_RGB2GRAY )
cv.ShowImage("converted-image", img_grayscale)

img_contour = cv.CreateImage(img_size, 8, 3)

# find the contours
contours = cv.FindContours(img_grayscale, storage, cv.CV_RETR_TREE, cv.CV_CHAIN_APPROX_SIMPLE, (0, 0))
for i in contours:
    print i
contours = cv.ApproxPoly (contours,storage,cv.CV_POLY_APPROX_DP, 8, 1)

levels = 2

# first, clear the image where we will draw contours
cv.SetZero(img_contour)

# initialisation
_contours = contours

# draw contours in red and green
cv.DrawContours(img_contour, #dest image
    _contours, #input contours
    _red, #color of external contour
    _green, #color of internal contour
    levels, #maxlevel of contours to draw
    _contour_thickness,
    cv.CV_AA, #line type
    (0, 0)) #offset

cv.NamedWindow("contours", 1)
# finally, show the image
cv.ShowImage("contours", img_contour)

cv.WaitKey(0)
