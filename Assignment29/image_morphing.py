import cv2 
import numpy as np

rock = cv2.imread("inputs/rock.jpg")
vin = cv2.imread("inputs/vin.jpg")

rock = cv2.cvtColor(rock, cv2.COLOR_BGR2GRAY)
vin = cv2.cvtColor(vin, cv2.COLOR_BGR2GRAY)

rock = cv2.resize(rock,(180,270))
vin = cv2.resize(vin,(180,270))

rock = rock.astype("float32")
vin = vin.astype("float32")

result2 = (rock*3/4 + vin*1/4) 
result3 = (rock*2/4 + vin*2/4) 
result4 = (rock*1/4 + vin*3/4) 


all = np.concatenate((rock,result2,result3,result4,vin),1)
result = all.astype("uint8")
cv2.imwrite("output/img_morphing.jpg",result)




