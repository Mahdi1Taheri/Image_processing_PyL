import numpy as np
import cv2

def bounding_rect(contour):
    if len(contour) < 3:
        return None
    
    min_x, max_x = float('inf'), float('-inf')
    min_y,max_y = float('inf'), float('-inf')

    for x,y in contour:
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)

    width = max_x - min_x
    height = max_y - min_y

    return  (min_x,min_y), width, height

