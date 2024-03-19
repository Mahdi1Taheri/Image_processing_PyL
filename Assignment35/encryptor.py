from PIL import Image
import random
import matplotlib.pyplot as plt


def encrypt():
    key = random.randint(0,200)
    path = open('input/face_color.jpg','rb')
    img = path.read()
    path.close()
    
    path_key = open('output/key.npy','wb')
    path_key.write(bytes([key]))
    img_data = bytearray(img)

    for index, value in enumerate(img_data):
        img_data[index] = value ^ key

    path = open('output/face_color_enc.bmp','wb')
    img_encrypt = path.write(img_data)
    path.close()
    
    plt.plot(img_data)
    plt.show()

encrypt()









# num = int(input('Enter number to Encrypt: '))
# key = int(input('Enter key: '))

# encrypted = num ^ key
# print(bin(num)[2:])
# print(bin(key)[2:])
# print(bin(encrypted)[2:])
# print(encrypted^key)