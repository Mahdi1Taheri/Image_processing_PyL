import cv2
import numpy as np

# input image for detect cats
img = cv2.imread("inputs\cat3.jpg")

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")
faces = face_detector.detectMultiScale(img)

if len(faces) > 1:
    print(f"There are {len(faces)} cats in this picture.")
elif len(faces) == 1:
    print(f"There are {len(faces)} cat in this picture.")
else:
    print("cat wasn't detect in this photo")

