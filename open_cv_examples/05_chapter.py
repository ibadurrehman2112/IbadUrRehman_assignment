# converting video into gray or black and white format  
import cv2 as cv
from numpy import binary_repr

cap = cv.VideoCapture('resources_01/video01.mp4')

while(True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    # to show in player
    if ret == True:
        cv.imshow("Video", binary)
        # to quit with (q) key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break