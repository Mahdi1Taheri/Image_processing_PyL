import cv2
import numpy as np

img1 = cv2.imread(...)
img2 = cv2.imread(...)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1 = img1 / 255.0

result = cv2.multiply(img1,img2)
 