import cv2
import numpy as np

img = cv2.imread('input/puma.jpg')
def reconstruct_image_from_histogram(histogram):

    hist_norm = histogram / np.sum(histogram) 
    cum_hist = np.cumsum(hist_norm)

    img = np.zeros((256, 256), dtype=np.uint8)  
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gray_level = np.argmax(cum_hist >= np.random.rand()) 
            img[i, j] = gray_level

    return img

# hist =  np.random.normal(10,10,10)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
reconstructed_img = reconstruct_image_from_histogram(hist)
cv2.imshow("Reconstructed Image", reconstructed_img)
cv2.waitKey(0)