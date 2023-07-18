import cv2
import numpy as np

# load the image and display it
image = np.ones((300, 300, 3), dtype=np.uint8) 

# draw a green horizontal line in the middle

color = (10, 250, 250)
thickness = 7
cv2.line(image, (125, 161), (127,122), color, thickness)
cv2.line(image, (127, 122), (146,160), color, thickness)
cv2.line(image, (146,160), (161,122), color, thickness)
cv2.line(image, (162,122), (165,161), color, thickness)

cv2.imshow("Line", image)
cv2.waitKey()
cv2.imwrite("name_design.jpg", image)
