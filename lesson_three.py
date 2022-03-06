import cv2

video = cv2.VideoCapture('cat.MP4')



while True:
    
    rep , frame = video.read()
    
    if rep:
        
        frame = cv2.resize(frame,(0,0),fx=1.2,fy=1.2)
        
        cv2.imshow('video',frame)  

    else:
        
        break
    
    if cv2.waitKey(20) == ord('q'):
        
        break

