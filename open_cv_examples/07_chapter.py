# How to capture a webcame inside python 
# step 1 import libraries
import cv2 as cv 
import numpy as np 
# step 2 Read the frames from Camera
cap = cv.VideoCapture(0) #webcam no. 1

if (cap.isOpened() == False):
    print("There is an error")

# step 3 Display frame by frame
while(cap.isOpened()):
    # capture frame by frame 
    ret, frame = cap.read()
    if ret == True:
        #to display frame 
        cv.imshow("Frame", frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# step 4 release or close windows easily 
cap.release()
cv.destroyAllWindows