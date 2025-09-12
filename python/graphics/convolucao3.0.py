import numpy as np
import cv2
import time

IMG_PATH = "templo1.jpg" #Path da imagem
img = np.array(cv2.imread(IMG_PATH))

kernel_sharpen = np.array([[0,-1,0],
                    [ -1, 5, -1],
                    [ 0, -1, 0]])

kernel_sobel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

kernel_blur = np.ones((3,3), np.float32) / 9

def convolution(image, kernel):

    input_height, input_width, channels = image.shape
    kernel_height, kernel_width = kernel.shape

    # padding para manter o mesmo tamanho
    pad_h, pad_w = kernel_height // 2, kernel_width // 2
    padded = np.pad(image,
                    ((pad_h, pad_h), (pad_w, pad_w), (0, 0)),
                    mode='constant')

    # saída do mesmo tamanho e tipo
    convolved_image = np.zeros_like(image, dtype=np.float32)

    for c in range(channels):
        for i in range(input_height):
            for j in range(input_width):
                region = padded[i:i+kernel_height, j:j+kernel_width, c]
                convolved_image[i, j, c] = np.sum(region * kernel)

    # clipping + volta para uint8
    convolved_image = np.clip(convolved_image, 0, 255).astype(np.uint8)
    return convolved_image

start_time = time.time()
img2 = convolution(img, kernel_sharpen)

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

img3 = cv2.filter2D(img,-1,kernel_sharpen)

print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow("djf",img)
cv2.imshow('32',img2)
cv2.imshow('843',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()