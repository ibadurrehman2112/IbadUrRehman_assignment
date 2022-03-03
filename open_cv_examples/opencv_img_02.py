# from msilib.schema import Binary
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
img = cv.imread("resources_01/image.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
binary = cv.resize(binary, (400, 500))
imwrite("resources_01/image_gray.png", gray)
imwrite("resources_01/image_bw.png", binary)