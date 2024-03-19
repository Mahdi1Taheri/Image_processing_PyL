import cv2
import numpy as np

room = cv2.imread('inputs/room.jpg')
floor = cv2.imread('inputs/floor.jpg')
room_mask = cv2.imread('inputs/room_mask.jpg')

result = cv2.bitwise_and(room_mask,floor)
result1 = cv2.bitwise_and(255 - room_mask,room)
final = cv2.add(result1,result)

cv2.imwrite('output/virtual_decoration.jpg',final)
