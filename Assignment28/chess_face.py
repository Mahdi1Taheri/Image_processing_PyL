import cv2

cap = cv2.VideoCapture('inputs\man.webm')


while True:
    _,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(frame)

    for face in faces:
        x,y,w,h = face
        face_img = frame[y:y+h , x:x+w]
        face_img_small = cv2.resize(face_img, [30,30])
        face_img_big = \
        cv2.resize(face_img_small,[w,h], interpolation= cv2.INTER_NEAREST)

        frame[y:y+h, x:x+w] = face_img_big
    
    cv2.imshow("",face_img_big)
    if cv2.waitKey(25) & 0xff == ord('q'):
        break
