import cv2
from matplotlib.pyplot import gray

img = cv2.imread('image_person.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray,(1.1), 3)
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img , (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('img',img)
cv2.waitKey(0)

