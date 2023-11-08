import cv2
import numpy as np
import os

while True:
    count = 1
    images_path = os.listdir(f'inputs/galaxy/{str(count)}')

    images = []

    for image_path in images_path:
        image = cv2.imread(f'inputs/galaxy/{str(count)}/' + image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros(image.shape)

    for image in images:
        result += image

    result = result / len(images)
    result = result.astype(np.uint8)

    cv2.imwrite(f"output/result{str(count)}.jpg", result)
    count += 1
    if count == 5:
        break
