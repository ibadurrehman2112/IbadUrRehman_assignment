# how to change the prespective of an image 
import cv2 as cv
import numpy as np 

img = cv.imread('resources_01/image.png')
print(img.shape) #(577, 433, 3)
## defining points
point1 = np.float32([[35,130],[390,18],[39,535],[402,531]])
width = 800
height = 900
width, height = 800, 900
point2 = np.float32([[0,0],[width,0],[0,height],[width, height]])

matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Original", img)
cv.imshow("transformed", out_img)
cv.waitKey(0)
cv.destroyAllWindows()
