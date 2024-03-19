import cv2

img = cv2.imread("images/my_pic.jpg")
thickness = 100
cv2.line(img,(-10,200),(233,-10),(0,0,0), thickness)
cv2.imshow("black_tape",img)
cv2.waitKey()
cv2.imwrite("black_tape.jpg",img)
