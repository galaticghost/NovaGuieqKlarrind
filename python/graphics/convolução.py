import numpy as np
from PIL import Image
from matplotlib import pyplot

IMG_PATH = "atitus1-small.png" #Path da imagem
img = np.array(Image.open(IMG_PATH).convert("L"))

kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

#Isso daqui funciona, mas só com um canal
def convolution(image, kernel):

    input_height, input_width = image.shape
    kernel_height, kernel_width = kernel.shape

    convolved_image = np.zeros((input_height - kernel_height + 1,
                                 input_width - kernel_width + 1))
    
    for i in range(0,len(convolved_image) ):
        for j in range(0, len(convolved_image[0])):
            for ii in range(0, kernel_height):
                for jj in range(0, kernel_width):
                  convolved_image[i,j] += image[i+ii, j+jj] * kernel[ii,jj]
    
    return convolved_image

img2 = convolution(img, kernel)

pyplot.imshow(img2,cmap='gray')
pyplot.show()