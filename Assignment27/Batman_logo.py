import cv2
import numpy as np

img = cv2.imread("Assignment27/bat.jpg")

img = cv2.cvtColor(img,cv2. COLOR_RGB2GRAY)
gg,img = cv2.threshold(img,220,255, cv2.THRESH_BINARY)
cv2.putText(img,"Batman",(60,190), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale= 1, color=(0,0,0))

cv2.imshow("result",img)
cv2.waitKey()
cv2.imwrite("Batman_logo.jpg", img)