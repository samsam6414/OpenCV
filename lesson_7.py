import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)

cv2.line(img, (0,0), (img.shape[1], img.shape[0]),(0, 255, 0), 10)
cv2.rectangle(img ,(0,0), (400,200),(0,0,255), cv2.FILLED) 

cv2.rectangle(img ,(80,140), (520,460),(255,255,255), cv2.FILLED)
cv2.circle(img, (300,300), 100, (0,0,255), cv2.FILLED)
cv2.putText(img , 'I LOVE JK',0( 30 , 100 ), cv2.FONT_HERSHEY_COMPLEX , 1 , (255,255,255),3)

cv2.imshow('img',img)

cv2.waitKey(0)
