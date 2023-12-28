import numpy as np 
import cv2

img = cv2.imread('input/flower_input.jpg',cv2.IMREAD_GRAYSCALE)

_,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
thresh = 255 - thresh1

blur = cv2.blur(img,(25,25),0)

res1 = cv2.bitwise_and(thresh,img)
bg = cv2.subtract(blur,res1)
res2 = cv2.bitwise_and(bg,thresh1)
final = cv2.add(res1,res2)

cv2.imwrite('output/foreground_focus.png',final)
