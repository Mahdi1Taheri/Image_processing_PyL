import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
# (480,640,3)
while True:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    roi = frame[200:300,280:360]
    blur = cv2.GaussianBlur(frame,(55,55),0)
    
    frame[:480,:280] = blur[:480,:280] 
    frame[:480,360:640] = blur[:480,360:640] 
    frame[:200,:640] = blur[:200,:640] 
    frame[300:480,:640] = blur[300:480,:640] 
    
    frame[200:300,280:360] = roi

    r = np.mean(roi[:,:,0])
    g = np.mean(roi[:,:,1])
    b = np.mean(roi[:,:,2])

    if 240 > r > 140 and g < 90 and b < 90 :
        text = 'COLOR: RED'
    elif 132 > r > 1 and 216 > g > 85 and 255 > b > 124:
        text = 'COLOR: BLUE'
    elif r < 100 and g > 150 and b < 100:
        text = 'COLOR: GREEN'
    elif r < 100 and g < 100 and b < 100:
        text = 'COLOR: BLACK'
    elif r > 100 and g > 100 and b > 100:
        text = 'COLOR: WHITE'
    elif 240 > r > 150 and 225 > g > 120 and 8 < b < 115:
        text = 'COLOR: YELLOW'
    elif 250 > r > 150 and 180 > g > 95 and  b < 51:
        text = 'COLOR: ORANGE'
    elif 210 > r > 70 and 80 > g and  130 < b < 250:
        text = 'COLOR: PURPLE'
    else:
        text = 'COLOR: UNDEFINED'
    

    cv2.putText(frame,text,(10,40),fontScale=1,color=0,thickness=3,fontFace=cv2.FONT_ITALIC)
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    rect = cv2.rectangle(frame,(280,200),(360,300),(0,0,0),2)
    cv2.imshow("",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

