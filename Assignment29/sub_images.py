import cv2
import numpy as np

img1 = cv2.imread(...)
img2 = cv2.imread(...)

result = cv2.subtract(img1,img2)