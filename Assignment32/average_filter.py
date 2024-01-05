import cv2 
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('input/1.tif')

kernel1 = np.ones((5,5),np.float32)/0.04
kernel2 = np.ones((5,5),np.float32)/1.0
kernel3 = np.ones((5,5),np.float32)/5.0
kernel4 = np.ones((3,3),np.float32)/0.04
kernel5 = np.ones((3,3),np.float32)/1.0
kernel6 = np.ones((3,3),np.float32)/5.0

dst1 = cv2.filter2D(img,-1,kernel1)
dst2 = cv2.filter2D(img,-1,kernel2)
dst3 = cv2.filter2D(img,-1,kernel3)
dst4 = cv2.filter2D(img,-1,kernel4)
dst5 = cv2.filter2D(img,-1,kernel5)
dst6 = cv2.filter2D(img,-1,kernel6)


fig = plt.figure(figsize=(10, 7)) 

rows = 2
columns = 3

fig.add_subplot(rows, columns, 1) 
plt.imshow(dst1) 
plt.title("1") 

fig.add_subplot(rows, columns, 2) 
plt.imshow(dst2) 
plt.title("2") 

fig.add_subplot(rows, columns, 3) 
plt.imshow(dst3) 
plt.title("3") 

fig.add_subplot(rows, columns, 4) 
plt.imshow(dst4) 
plt.title("4") 

fig.add_subplot(rows, columns, 5) 
plt.imshow(dst5) 
plt.title("5") 

fig.add_subplot(rows, columns, 6) 
plt.imshow(dst6) 
plt.title("6") 

fig.savefig('output/fig_magic.png')
# plt.waitforbuttonpress()

# Adds a subplot at the 3rd position 
