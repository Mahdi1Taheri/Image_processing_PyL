import cv2
import numpy as np

img = cv2.imread('input\spiderman.png')
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(img_hsv)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (h[i,j] < 5 or h[i,j] > 170) and s[i,j] > 140 :
            h[i,j] += 65
            
        if 95 < h[i,j] < 130 and s[i,j] > 100:
            h[i,j] -= 75
            v[i,j] += 25
           

img_hsv = cv2.merge((h,s,v))
img_hsv = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
imgs = np.hstack((img,img_hsv))
cv2.imwrite("output/spiderman.png",imgs)