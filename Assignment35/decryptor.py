import matplotlib.pyplot as plt


def decrypt():
    key = 'output/key.npy'
    path = open('output/face_color_enc.bmp','rb')
    img = path.read()
    path.close()
    
    key_path = open(key,'rb')
    key = key_path.read()
    key_path.close()
    key = int.from_bytes(key)

    img_data = bytearray(img)

    for index, value in enumerate(img_data):
        img_data[index] = value ^ key

    path = open('output/face_color_dec.jpg','wb')
    img_encrypt = path.write(img_data)
    path.close()


decrypt()


