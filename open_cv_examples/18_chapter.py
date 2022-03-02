# split your video into frames or image sequence 

import cv2 as cv

cap = cv.VideoCapture("resources_01/video01.mp4")

frameNr = 0

while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"resources_01/frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+1
    # frameNr = frameNr+2       more frames 
cap.release()