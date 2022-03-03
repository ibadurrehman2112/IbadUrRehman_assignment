# reading a vedio 
import cv2 as cv

cap = cv.VideoCapture('resources_01/video01.mp4')
# indicator
if (cap.isOpened() == False):
    print("error in reading video")

# reading and playing 

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

