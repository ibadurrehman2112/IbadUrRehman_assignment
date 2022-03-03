# Face detection
import cv2 as cv


face_cascade = cv.CascadeClassifier('resources_01/haarcascade_frontalface_default.xml')
img = cv.imread("resources_01/image.png")
# img = cv.resize(img, (200, 275)) # resizing the image
# print(img.shape)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

#draw a rectangle
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)


cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()