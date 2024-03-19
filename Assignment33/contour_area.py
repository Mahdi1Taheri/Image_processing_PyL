import numpy as np
import cv2
def contour_area(contour):
    if len(contour) < 3:
        return 0
    
    area = 0
    for i in range(len(contour)):
        x1,y1 = contour[i]
        x2,y2 = contour[(i+1) % len(contour)]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2

contour = [(1,1),(2,3),(4,2),(3,1)]
print(contour_area(contour))
contour2 = np.array([[[1,1]], [[2,3]], [[4,2]], [[3,1]]])
print(cv2.contourArea(contour2))
