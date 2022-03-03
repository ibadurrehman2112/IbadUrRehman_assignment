# converting video into gray format  
import cv2 as cv

cap = cv.VideoCapture('resources_01/video01.mp4')

while(True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret == True:
        cv.imshow("Video", grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break