import cv2

cap=cv2.VideoCapture(0)

while True:
    _,camera=cap.read()
    gray=cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
    _,biner=cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
    
    cv2.imshow('Camera',camera)
    cv2.imshow('Grayscale',gray)
    cv2.imshow('B&W',biner)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()