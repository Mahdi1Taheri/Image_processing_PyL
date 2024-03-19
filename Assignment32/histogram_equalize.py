import cv2
import numpy as np

img1 = cv2.imread('input/land.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('input/up.webp',cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('input/pic1.webp',cv2.IMREAD_GRAYSCALE)


result1 = cv2.equalizeHist(img1)
result2 = cv2.equalizeHist(img2)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res = clahe.apply(img3)

result1 = np.hstack((img1,result1))
result2 = np.hstack((img2,result2))
res = np.hstack((img3,res))

cv2.imwrite('output/equalize1.png',result1)
cv2.imwrite('output/equalize2.png',result2)
cv2.imwrite('output/equalize_clahe.png',res)



