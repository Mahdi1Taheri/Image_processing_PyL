import cv2
import numpy as np
import matplotlib.pyplot as plt

balloon_img = cv2.imread('input/baloon.jpg')
balloon_img = cv2.cvtColor(balloon_img, cv2.COLOR_BGR2HSV)

lower_hue = np.array([160,0,0]) 
upper_hue = np.array([180,255,255])
mask = cv2.inRange(balloon_img, lower_hue, upper_hue)
balloon_img = cv2.cvtColor(balloon_img,cv2.COLOR_HSV2RGB)
balloon_img = cv2.bitwise_and(balloon_img,balloon_img,mask=mask)

cv2.imwrite('output/balloon_detection.png',balloon_img)