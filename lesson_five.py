import cv2

img = cv2.imread('no.jpg')
img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
new_img = img[:100,:200]

cv2.imshow('img',img)
cv2.imshow('new_img',new_img)
cv2.waitKey(0)
