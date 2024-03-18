import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

# (480,640,3)
while True:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    roi = frame[200:300,280:360]
    blur = cv2.GaussianBlur(frame,(55,55),0)
    
    frame[:480,:280] = blur[:480,:280] 
    frame[:480,360:640] = blur[:480,360:640] 
    frame[:200,:640] = blur[:200,:640] 
    frame[300:480,:640] = blur[300:480,:640] 

    H, S, V = cv2.split(roi)
    mean_h=np.mean(H)
    mean_s=np.mean(S)
    mean_v=np.mean(V)


    if  (mean_h < 15 or mean_h > 170) and mean_s > 50 and mean_v > 100:
        text = 'COLOR:RED'
    elif (95 < mean_h < 125) and mean_s > 30 and mean_v > 100:
        text = 'COLOR: BLUE'
    elif 35 < mean_h < 80 and mean_s > 50 and mean_v > 100:
        text = 'COLOR: GREEN'
    elif mean_v < 100:
        text = 'COLOR: BLACK'
    elif mean_s < 50 and mean_v > 80:
        text = 'COLOR: WHITE'
    elif 20 < mean_h < 35 and mean_s > 80 and mean_v > 60:
        text = 'COLOR: YELLOW'
    elif 15 < mean_h < 30 and mean_s > 80  and  mean_v > 50:
        text = 'COLOR: ORANGE'
    elif 130 < mean_h < 175 and 50 < mean_s and  mean_v > 50:
        text = 'COLOR: PURPLE'
    else:
        text = 'COLOR: UNDEFINED'
    

    cv2.putText(frame,text,(10,40),fontScale=1,color=0,thickness=3,fontFace=cv2.FONT_ITALIC)
    frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    rect = cv2.rectangle(frame,(280,200),(360,300),(0,0,0),2)

    cv2.imshow('',frame)
 

    if cv2.waitKey(25) & 0xFF==ord('q') :
        break

cap.release()
