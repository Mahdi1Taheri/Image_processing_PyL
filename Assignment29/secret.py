import cv2
import numpy as np

img1 = cv2.imread('inputs/a.png')
img2 = cv2.imread('inputs/b.png')

result = cv2.subtract(255-img1,255-img2)
cv2.imwrite("output/secret.jpg",result)