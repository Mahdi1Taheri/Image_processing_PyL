import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    histogram = np.zeros(256, dtype=int)

    for i in range(h):
        for j in range(w):
            pixel_value = gray[i, j]
            
            histogram[pixel_value] += 1
    
    return histogram

image = cv2.imread('input/brad.jpg')
histogram = calculate_histogram(image)

plt.hist(image.ravel(),256)
plt.xlabel('Pixel value')
plt.ylabel('Number of pixels')
plt.title('Histogram of image(hist)')
plt.show()

plt.plot(histogram)
plt.xlabel('Pixel value')
plt.ylabel('Number of pixels')
plt.title('Histogram of image(plot)')
plt.show()

plt.bar(range(256), histogram)
plt.xlabel('Pixel value')
plt.ylabel('Number of pixels')
plt.title('Histogram of image(bar)')
plt.show()



