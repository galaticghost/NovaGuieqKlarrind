import numpy as np
import cv2

IMG_PATH = "3.jpg" #Path da imagem
img = np.array(cv2.imread(IMG_PATH))

kernel = np.array ([[0.003,  0.013,  0.022,  0.013,  0.003],
                    [0.013,  0.059,  0.097,  0.059,  0.013],
                    [0.022,  0.097,  0.159,  0.097,  0.022],
                    [0.013,  0.059,  0.097,  0.059,  0.013],
                    [0.003,  0.013,  0.022,  0.013,  0.003]])


def convolution(image, kernel):

    input_height, input_width, channels = image.shape
    kernel_height, kernel_width = kernel.shape

    convolved_image = np.zeros((input_height - kernel_height + 1,
                                 input_width - kernel_width + 1,
                                 channels))
    
    for c in range(channels):
        for i in range(0,len(convolved_image) ):
            for j in range(0, len(convolved_image[0])):
                for ii in range(0, kernel_height):
                    for jj in range(0, kernel_width):
                        convolved_image[i,j,c] += image[i+ii, j+jj,c] * kernel[ii,jj]
    
    return convolved_image

img2 = convolution(img, kernel)
img3 = cv2.filter2D(img,-1,kernel)
cv2.imshow('32',img2)
cv2.imshow('843',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()