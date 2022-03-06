import cv2

img = cv2.imread('no.jpg')

img = cv2.resize(img,(0,0), fx = 0.3, fy =0.3)

cv2.imshow('img',img)

cv2.waitKey(0)