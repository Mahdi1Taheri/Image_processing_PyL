import cv2

cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('video', frame)

    
    if cv2.waitKey(25) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()