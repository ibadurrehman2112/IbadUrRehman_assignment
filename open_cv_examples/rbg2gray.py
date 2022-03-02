# import library 
import cv2 as cv
from cv2 import cvtColor

img = cv.imread("resources_01/image01.jpg")
img = cv.resize(img,(800,600))

#conversion
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

# displaycode 
cv.imshow("First image", img)
cv.imshow("Gray Image", gray_img)

# delay code
cv.waitKey(0)
cv.destroyAllWindows()