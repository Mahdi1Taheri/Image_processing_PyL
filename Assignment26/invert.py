import cv2


image = cv2.imread("images/2.jpg")

inverted = cv2.bitwise_not(image)
cv2.imshow("Inverted", inverted)
cv2.waitKey()

cv2.imwrite("inverted_img.jpg", inverted)
