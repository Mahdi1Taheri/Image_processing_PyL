import cv2
import numpy as np

img = cv2.imread('input/bronzino.webp')
cap = cv2.VideoCapture(1)

img_height,img_width,_ = img.shape

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'frame width:{frame_width},frame height:{frame_height}')
print(f'image width:{img_width},image height:{img_height}')

y = 50
x = 50

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('frame',img)
    img[300:400,350:500] = frame[300:400,400:550]
    frame = img


    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()