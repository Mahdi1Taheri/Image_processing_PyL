import cv2
import numpy as np
import os

lst = []
count = 1
while True:
    images_path = os.listdir(f'inputs/galaxy/{str(count)}')

    images = []

    for image_path in images_path:
        image = cv2.imread(f'inputs/galaxy/{str(count)}/' + image_path)
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros(image.shape)

    for image in images:
        result += image

    result = result / len(images)
    result = result.astype(np.uint8)

    if os.path.isdir('output/galaxy'):
        pass
    else: 
        os.mkdir("output/galaxy")
    cv2.imwrite(f"output/galaxy/result{str(count)}.jpg", result)
    count += 1
    if count == 5:
        galaxy_imgs = os.listdir('output/galaxy/')
        for i in galaxy_imgs:
            read_imgs = cv2.imread("output/galaxy/" + i)
            lst.append(read_imgs)
        all0 = np.concatenate((lst[0],lst[2]),0)
        all1 = np.concatenate((lst[1],lst[3]),0)
        all = np.concatenate((all0,all1),1)
        
        cv2.imwrite("output/galaxy/final.jpg",all)
        break
