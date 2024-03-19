import cv2 
import numpy as np
import imageio

# while True:
tv_img = cv2.imread("Assignment27\old_tv.jpg")
tv_img2 = cv2.cvtColor(tv_img,cv2.COLOR_RGB2GRAY)
rows, col = tv_img2.shape
img_lst = []


video_writer = cv2.VideoWriter("TV_Noise.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (col, rows))

while True:
    blank_img = np.random.random((265,340)) * 255
    noises = np.array(blank_img, dtype= np.uint8)
    tv_img2 = cv2.cvtColor(tv_img,cv2.COLOR_BGR2GRAY)
    tv_img2[45:310,40:380] = noises
    # for i in range(20):
    #     img_lst.append(tv_img1)
    images = tv_img2.astype(np.uint8)
    img_lst.append(images)

    video_writer.write(tv_img2)
    cv2.imshow("",tv_img2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video_writer.release()
imageio.mimsave('noise.gif', img_lst)









