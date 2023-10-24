import cv2

img = cv2.imread("face.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_detector.detectMultiScale(img_gray)

for face in faces:
    x,y,w,h = face
    face_img = img[y:y+h , x:x+w]
    face_img_small = cv2.resize(face_img, [30,30])
    face_img_big = \
    cv2.resize(face_img_small,[w,h], interpolation= cv2.INTER_NEAREST)

    img[y:y+h, x:x+w] = face_img_big
    
cv2.imshow("",face_img_big)
cv2.waitKey()