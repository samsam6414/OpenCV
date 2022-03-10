import cv2
import numpy as np
import random as rd

#快速註解 Shift + Alt + A 

img = cv2.imread('yes.jpg')
img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)

#print(img.shape) 

#img = np.empty((300,300,3), np.uint8 )

for row in range(100):
    for col in range(210):
        img[row][col] = [rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)]

cv2.imshow('img',img)
cv2.waitKey(0)    