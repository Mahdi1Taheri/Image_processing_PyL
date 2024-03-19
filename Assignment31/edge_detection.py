import cv2
import numpy as np

img = cv2.imread("input/lion.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows, cols = img.shape
result = np.zeros((rows,cols),dtype=np.uint8)

filter = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small = img[i-1:i+2,j-1:j+2]
        result[i,j] = np.abs(np.sum(filter*small))

cv2.imwrite("output/edge_detect.png",result)
