# Basic functions or manipulations in open cv 

import cv2 as cv
import numpy as np
img = cv.imread("resources_01/image.png")
# resize
resized_img = cv.resize(img, (350, 250))
# GRAY image 
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blurr image 
blurr_img = cv.GaussianBlur(img, (7,7), 0)
# edge detection
edge_img = cv.Canny(img, 48, 48)
# thickness of lines
mat_kernel = np.ones((7,7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel), iterations=1)
# dilated_img = cv.dilate(edge_img, (7,7), iterations=1)

# Make thiner outline 
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1) 

# cropping we will use numpy library not open cv 
print("The size of image is ", img.shape)
cropped_img = img[0:400, 0:300]





cv.imshow("Original", img)
cv.imshow("Resized", resized_img)
cv.imshow("Gray", gray_img)
cv.imshow("Blur", blurr_img)
cv.imshow("edge", edge_img)
cv.imshow("dilated", dilated_img)
cv.imshow("Erosion", ero_img)
cv.imshow("Cropped", cropped_img)


cv.waitKey(0)
cv.destroyAllWindows()