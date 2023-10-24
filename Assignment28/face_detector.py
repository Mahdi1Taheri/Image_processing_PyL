import cv2

cap = cv2.VideoCapture('inputs\man.webm')
sticker = cv2.imread('inputs\emoji.png',cv2.IMREAD_UNCHANGED)
eye_sticker = cv2.imread('inputs\sun-glasses.png')
lips_sticker = cv2.imread('inputs\kiss.png' )

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml ")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")


def apply_sticker(cap,sticker):
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            sticker_resized = cv2.resize(sticker, (w, h))
            for c in range(3):
                frame[y:y+h, x:x+w, c] = sticker_resized[:, :, c] * (sticker_resized[:, :, 3] / 255.0) + frame[y:y+h, x:x+w, c] * (1.0 - sticker_resized[:, :, 3] / 255.0)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def smile_eye_sticker(cap,eye_stk,lip_stk):
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
        # Extract the region of interest (ROI) containing the face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Detect eyes in the ROI
            eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
            lips = smile_cascade.detectMultiScale(roi_gray,1.3,5)

            for (ex, ey, ew, eh) in eyes:
                # Apply the sticker on both eyes
                glasses_resized = cv2.resize(eye_stk, (ew, eh))
                roi_color[ey:ey+eh, ex:ex+ew] = glasses_resized

            for (ex, ey, ew, eh) in lips:
                # Apply the sticker on both eyes
                lip_resized = cv2.resize(lip_stk, (ew, eh))
                roi_color[ey:ey+eh, ex:ex+ew] = lip_resized
        

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def mosaic_blur(cap):
    mosaic_size = 15

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            roi = cv2.resize(roi, (mosaic_size, mosaic_size), interpolation=cv2.INTER_LINEAR)
            roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = roi

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
def mirror_filter(video):
    while True:
        ret, frame = video.read()
        if not ret:
            break

        x = frame.shape[1]

        mirror_frame = frame.copy()
        mirror_frame[:, x // 2:] = cv2.flip(frame[:, :x // 2], 1)

        cv2.imshow('Mirrored Video', mirror_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# mosaic_blur(cap)
# apply_sticker(cap,sticker)
smile_eye_sticker(cap,eye_sticker,lips_sticker)\
# mirror_filter(cap)

cap.release()
cv2.destroyAllWindows()



