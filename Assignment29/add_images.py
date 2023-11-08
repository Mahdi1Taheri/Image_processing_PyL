import cv2
import numpy as np

image_human = cv2.imread("inputs/rock.jpg")
image_horse = cv2.imread("inputs/vin.jpg")

image_human = cv2.cvtColor(image_human, cv2.COLOR_BGR2GRAY)
image_horse = cv2.cvtColor(image_horse, cv2.COLOR_BGR2GRAY)

# result = image_human + image_horse
# result = cv2.add(image_human, image_horse)
# result = np.add(image_horse,image_human)

image_human = image_human.astype("float32")
image_horse = image_horse.astype("float32")

result = image_human + image_horse
result = result.astype("uint8")

cv2.imshow("", result)
cv2.waitKey()



