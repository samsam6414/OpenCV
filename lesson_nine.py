import cv2

img = cv2.imread('shape.jpg')
img = cv2.resize(img, (0,0), fx=2, fy=2)
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img, 150, 200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4)
    print(cv2.contourArea(cnt))


cv2.imshow('shape',img)
cv2.imshow('canny',canny)
cv2.imshow('imgContour',imgContour)
cv2.waitKey(0)