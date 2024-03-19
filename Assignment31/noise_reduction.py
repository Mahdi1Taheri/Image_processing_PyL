import cv2
import numpy as np

board_img = cv2.imread("input/board_noisy.png",cv2.IMREAD_GRAYSCALE)
circle_noisy = cv2.imread('input\image_noisy.png',cv2.IMREAD_GRAYSCALE)

def noise_reduction(img):
    rows,cols = img.shape
    result = np.zeros((rows,cols),dtype=np.uint8)

    filter = np.ones((3,3)) / 9

    for i in range(1,rows-1):
        for j in range(1,cols-1):
            small = img[i-1:i+2,j-1:j+2]
            average = np.sum(filter*small)
            result[i,j] = average
    
    return result


board_reduced = noise_reduction(board_img)
cv2.imwrite('output/board_noise_reduced.png',board_reduced)
circle_reduced = noise_reduction(circle_noisy)
cv2.imwrite('output/circle_noise_reduced.png',circle_reduced)
