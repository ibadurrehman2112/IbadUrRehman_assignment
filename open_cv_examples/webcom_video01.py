# Resolution of car 
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
# resolution  HD (1280x720)

# cap.set(3, 1280)
# cap.set(4, 720)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)
def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)

hd_resolution()
# sd_resolution()
# fhd_resolution()

# How to change and fix the frame rate to 30fps



while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Camera", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv.destroyAllWindows()