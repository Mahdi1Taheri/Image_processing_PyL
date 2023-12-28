import cv2
import numpy as np

img = cv2.imread("input/building.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows, cols = img.shape
result = np.zeros((rows,cols),dtype=np.uint8)
result2 = np.zeros((rows,cols),dtype=np.uint8)

filter_vertical = np.array([[-1, 0, 1],
                            [-2,  0, 2],
                            [-1, 0, 1]])

filter_horizontal = np.array([[1, 2, 1],
                            [0,  0, 0],
                            [-1, -2, -1]])

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small = img[i-1:i+2,j-1:j+2]
        result[i,j] = np.abs(np.sum(filter_vertical*small))
        result2[i,j] = np.abs(np.sum(filter_horizontal*small))

cv2.imwrite("output/vertical.png",result)
cv2.imwrite("output/horizontal.png",result2)

