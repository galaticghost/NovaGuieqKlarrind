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

kernel_outline = np.array([[ -1, -1, -1],
                        [ -1,  9, -1],
                        [ -1, -1, -1]])

kernel_emboss = np.array([[-2, -1,  0],
 [-1,  1,  1],
 [ 0,  1,  2]]
)

def convolution(img, kernel):

    input_height, input_width, channels = img.shape
    kernel_height, kernel_width = kernel.shape

    pad_h, pad_w = kernel_height // 2, kernel_width // 2
    padded = np.pad(img,((pad_h, pad_h), (pad_w, pad_w), (0, 0)))

    convolved_image = np.zeros_like(img, dtype=np.float32)

    for c in range(channels):
        for i in range(input_height):
            for j in range(input_width):
                region = padded[i:i+kernel_height, j:j+kernel_width, c]
                convolved_image[i, j, c] = np.sum(region * kernel)

    convolved_image = np.clip(convolved_image, 0, 255).astype(np.uint8)
    return convolved_image

def kernel_sharpen_convolution():
    print("Kernel:kernel sharpen")

    start_time = time.time()
    img2 = convolution(img, kernel_sharpen)
    print(f"{(time.time() - start_time)} segundos para o nosso algoritmo")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_sharpen)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel sharpen',img2)
    cv2.imshow('kernel sharpen openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kernel_blur_convolution():
    print("Kernel:kernel blur")

    start_time = time.time()
    img2 = convolution(img, kernel_blur)
    print(f"{(time.time() - start_time)} segundos para o nosso algoritmo")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_blur)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel blur',img2)
    cv2.imshow('kernel blur openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kernel_sobel_convolution():
    print("Kernel:kernel sobel")

    start_time = time.time()
    img2 = convolution(img, kernel_sobel)
    print(f"{(time.time() - start_time)} segundos para o nosso algoritmo")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_sobel)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel sobel',img2)
    cv2.imshow('kernel sobel openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def kernel_outline_convolution():
    print("Kernel:kernel outline")

    start_time = time.time()
    img2 = convolution(img, kernel_outline)
    print(f"{(time.time() - start_time)} segundos para o nosso algoritmo")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_outline)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel outline',img2)
    cv2.imshow('kernel outline openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kernel_emboss_diagonal_convolution():
    print("Kernel:kernel emboss diagonal")

    start_time = time.time()
    img2 = convolution(img, kernel_emboss)
    print(f"{(time.time() - start_time)} segundos para o nosso algoritmo")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_emboss)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel emboss diagonal',img2)
    cv2.imshow('kernel emboss diagonal openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

kernel_emboss_diagonal_convolution()

