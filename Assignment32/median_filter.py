import cv2
import numpy as np

# cv2.medianBlur()
img1 = cv2.imread('input/board_noisy.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('input/image_noisy.png',cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('input/bllon.webp')
img4 = cv2.imread('input/a.webp')
img5 = cv2.imread('input/a2.webp',cv2.IMREAD_GRAYSCALE)

result1 = cv2.medianBlur(img1,5)
result2 = cv2.medianBlur(img2,5)
result3 = cv2.medianBlur(img3,5)
result4 = cv2.medianBlur(img4,5)
result5 = cv2.medianBlur(img5,5)

result1 = np.hstack((img1,result1))
result2 = np.hstack((img2,result2))
result3 = np.hstack((img3,result3))
result4 = np.hstack((img4,result4))
result5 = np.hstack((img5,result5))

cv2.imwrite('output/result_median1.png',result1)
cv2.imwrite('output/result_median2.png',result2)
cv2.imwrite('output/result_median3.png',result3)
cv2.imwrite('output/result_median4.png',result4)
cv2.imwrite('output/result_median5.png',result5)
