import numpy as np
import cv2
import time
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel


lip_index = [52,55,56,53,59,58,61,68,67,71,63,64]
left_eye = [89,90,87,91,93,96,94,95]
right_eye = [39,42,40,41,35,36,33,37]

fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")

img = cv2.imread("input/face.jpg")

orange = cv2.imread('input/orange.png')
orange = cv2.resize(orange,(150,170))

color = (0, 0, 255)

start_time = time.perf_counter()

def big_img(img,indexes):
    boxes, scores = fd.inference(img)
    for pred in fa.get_landmarks(img, boxes):
        landmarks = []
        for i in indexes:
            landmarks.append(pred[i])
        landmarks = np.array(landmarks,dtype=int)
        print(landmarks)

    x,y,w,h = cv2.boundingRect(landmarks)

    mask = np.zeros(img.shape,dtype=np.uint8)
    cv2.drawContours(mask,[landmarks],-1,(255,255,255),-1)
    mask = mask // 255
    result = cv2.multiply(img,mask)

    result = result[y:y+h,x:x+w]
    result_big = cv2.resize(result,(0,0),fx=4,fy=4)
    print(time.perf_counter() - start_time)

    return result



lip = big_img(img,lip_index)
lip = cv2.resize(lip,(50,20))

eye_r = big_img(img,right_eye)
eye_r = cv2.resize(eye_r,(40,20))

eye_l = big_img(img,left_eye)
eye_l = cv2.resize(eye_l,(40,20))

# masking 
mask = np.zeros([90, 90, 3])
mask[0:20, 0:40 , 0:3] = eye_r
mask[0:20, 50:90] = eye_l
mask[30:50, 22:72] = lip


x, y, w, h = [37, 70, 90, 90]
for i in range(h):
    for j in range(w):
        if mask[i][j][0] == 0 and mask[i][j][1] == 0 and mask[i][j][2] == 0:
            mask[i][j] = orange[y+i,x+j]

orange[y:y+h,x:x+w] = mask


cv2.imwrite('output/fruit_filter.png',orange)
cv2.waitKey()


