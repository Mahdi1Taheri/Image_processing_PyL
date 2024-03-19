import numpy as np
import cv2

def find_contours(image, threshold=128):
  if len(image.shape) > 2:
    image = np.where(image > threshold, 255, 0)
  contours = []

  for y in range(image.shape[0]):
    for x in range(image.shape[1]):
      if image[y, x] == 255 and not image[y, x] == -1:
        contour = []
        dfs(image, y, x, contour)
        contours.append(contour)

  return contours

def dfs(image, y, x, contour):
  image[y, x] = -1
  contour.append((x, y))

  neighbors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
  for dy, dx in neighbors:
    if 0 <= dy < image.shape[0] and 0 <= dx < image.shape[1] and image[dy, dx] == 255:
      dfs(image, dy, dx, contour)

image = np.array([[0, 0, 255, 0],
                   [0, 255, 255, 0],
                   [0, 255, 0, 0]])
contours = find_contours(image)
print(contours)
