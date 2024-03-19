import cv2
import numpy as np

# Load the pre-trained eye and lip detection models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
lip_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')

# Load the sunglass and lip sticker images
sunglass_sticker = cv2.imread('inputs\sunglass.jpg')
lip_sticker = cv2.imread('inputs\kiss.png')

# Define a function to apply a sticker to an image
def apply_sticker(image, sticker, x, y):
    # Resize the sticker to match the size of the region of interest
    sticker = cv2.resize(sticker, (image.shape[1], image.shape[0]))

    # Create a mask for the sticker
    mask = cv2.threshold(sticker[:, :, 3], 1, 255, cv2.THRESH_BINARYINV)[1]

    # Apply the sticker to the image
    image = cv2.addWeighted(image, 1, sticker, 1, 0, mask=mask)

    return image

# Start the video capture
cap = cv2.VideoCapture('inputs\man.webm')

while True:
    # Capture the next frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop over the detected faces
    for (x, y, w, h) in faces:

        # Detect eyes in the face
        eyes = eye_cascade.detectMultiScale(gray[y:y + h, x:x + w])

        # Loop over the detected eyes
        for (ex, ey, ew, eh) in eyes:

            # Apply the sunglass sticker to the eye
            frame = apply_sticker(frame, sunglass_sticker, x + ex, y + ey)

        # Detect lips in the face
        lips = lip_cascade.detectMultiScale(gray[y:y + h, x:x + w])

        # Loop over the detected lips
        for (lx, ly, lw, lh) in lips:

            # Apply the lip sticker to the lip
            frame = apply_sticker(frame, lip_sticker, x + lx, y + ly)

    # Display the frame
    cv2.imshow('Video', frame)

    # Exit the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()
