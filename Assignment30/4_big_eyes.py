import numpy as np
import cv2
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel

fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")

lip_index = [52,55,56,53,59,58,61,68,67,71,63,64]
left_eye = [89,90,87,91,93,96,94,95]
right_eye = [39,42,40,41,35,36,33,37]

image = cv2.imread("input/face.jpg")

def big_eyes_lip(indexes, img):
    boxes, scores = fd.inference(img)
    for pred in fa.get_landmarks(img, boxes):
        landmarks = []
        for i in indexes:
            landmarks.append(pred[i])
        landmarks = np.array(landmarks,dtype=int)

    x, y, w, h = cv2.boundingRect(landmarks)
    mask = np.zeros(img.shape, dtype=np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (255, 255, 255), -2)
    mask = mask // 255

    result = cv2.multiply(img,mask)
    result = result[y:y+h, x:x+w]
    doubled = cv2.resize(result, (w*2, h*2))

    for i in range(h*2):
        for j in range(w*2):
            if doubled[i][j][0] == 0 and doubled[i][j][1] == 0 and doubled[i][j][2] == 0:
                doubled[i][j] = image[int(y-h//2)+i, int(x-w//2)+j]

    img[int(y-h//2):int(y-h//2)+h*2, int(x-w//2):int(x-w//2)+w*2] = doubled

    return img

result = big_eyes_lip(lip_index, image)
result = big_eyes_lip(right_eye, image)
result = big_eyes_lip(left_eye, image)

cv2.imshow("result", result)
cv2.waitKey()
cv2.imwrite("output/big_eyes_face.jpg", result)