import cv2
import numpy as np


img = np.ones((260, 300, 3), dtype=np.uint8) * 255
c = 10
for i in range(300):
    img[i:i+1,0:300] = c
    c -= 1

cv2.imshow("gradient",img)
cv2.waitKey()
cv2.imwrite("gradient.jpg",img)


