import cv2
import numpy as np

img = np.ones((400, 400, 3), dtype=np.uint8) * 250

cell_size = 50
for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 == 0:
            cv2.rectangle(img, (i * cell_size, j * cell_size), ((i + 1) * cell_size, (j + 1) * cell_size), (0,0,0), -1)

cv2.imshow("Chess Board", img)
cv2.waitKey(0)
cv2.imwrite("chess_board.jpg", img)
