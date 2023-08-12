import cv2
import time
import numpy as np
import imageio

# Create a black image
img = cv2.imread("Assignment27\winter-house.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img,(600,400))
new_img = img.copy()
frames = []
alpha = 0.4


# Draw some white snowflakes
while True:
    for i in range(500):
        x = np.random.randint(0, 600)
        y = np.random.randint(0, 400)
        dst = cv2.circle(img, (x,y), 1, (255,255,255), -1)

        # Reduce transparency of snows to look natural :)
        image_new = cv2.addWeighted(new_img, alpha, dst, 1 - alpha, 0)

    img = cv2.imread("Assignment27\winter-house.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,(600,400))
    frames.append(image_new)
        
    
    time.sleep(0.01)
    cv2.imshow("result", image_new)
    if cv2.waitKey(25) & 0xff == ord("q"):
        break

imageio.mimsave('snowfall.gif', frames)


