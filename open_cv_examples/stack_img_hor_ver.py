# Joining two images
from tabnanny import verbose
import cv2  as cv
import numpy as np

img = cv.imread("resources_01/image.png")

# stacking same image 

#1- Horizental stack

hor_img = np.hstack((img, img))

#2- Verticle stack

ver_img = np.vstack((img, img))

cv.imshow("Horizental", hor_img)
cv.imshow("Vertical", ver_img)
cv.waitKey(0)
cv.destroyAllWindows()

# you can only stack images with same shape (width, Height, color channel)
# we can not resize the stack image (function)
# same number of channels np function
# (600, 500, 3)
# you have to define a function to stack nultiple images of different sizes and tunes