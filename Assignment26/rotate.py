import cv2

my_img = cv2.imread("images/3.jpg")
rotated_img = cv2.rotate(my_img, cv2.ROTATE_180)
# cv2.resize(new,(500,700))

cv2.imshow("rotation",rotated_img)
cv2.waitKey()
cv2.imwrite("rotate180.jpg",rotated_img)
