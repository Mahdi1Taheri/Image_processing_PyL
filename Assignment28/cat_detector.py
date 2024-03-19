import cv2
import numpy as np

img = cv2.imread("inputs\cats.jpeg")

catface_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
faces = catface_detector.detectMultiScale(img)

for cat_face in faces:
    x, y, w, h = cat_face
    cv2.rectangle(img, [x, y], [x+w, y+h], (100, 200, 100), 5)

cv2.imshow("",img)
cv2.waitKey()

if len(faces) > 1:
    print(f"There are {len(faces)} cats in this picture.")
elif len(faces) == 1:
    print(f"There are {len(faces)} cat in this picture.")
else:
    print("cat wasn't detect in this photo")
