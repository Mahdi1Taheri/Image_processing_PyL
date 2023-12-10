import numpy as np
import cv2
import time
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel

start_time = time.perf_counter()

lip_index = [52,55,56,53,59,58,61,68,67,71,63,64]
left_eye = [89,90,87,91,93,96,94,95]
right_eye = [39,42,40,41,35,36,33,37]

fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")

def separator(img,indexes):
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
    result = cv2.flip(result,0)
    roi = img[y:y+h,x:x+w]

    overlaid_image = cv2.addWeighted(roi, 0.5, result, 1, 0)
    img[y:y+h, x:x+w] = overlaid_image

    print(time.perf_counter() - start_time)

    return img

img = cv2.imread('input/face.jpg')

lip = separator(img,lip_index)
eye_rht = separator(img,right_eye)
eye_lft = separator(img,left_eye)

rotated_image=cv2.flip(lip, 0)


cv2.imwrite("output/rotated_img.jpg",rotated_image)