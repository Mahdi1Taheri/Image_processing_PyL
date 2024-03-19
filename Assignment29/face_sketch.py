import numpy as np
import cv2

img = cv2.imread('inputs\pedro.jpg')
kernel_sharpening = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]]) 
sharpened = cv2.filter2D(img,-1,kernel_sharpening)
img = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
inverted = 255 - img
blurred = cv2.GaussianBlur(inverted,(15,15),sigmaX=0,sigmaY=0)
sketch = cv2.divide(img,255-blurred)
sketch = sketch * 255

cv2.imwrite('output/sketch_face.jpg', sketch)