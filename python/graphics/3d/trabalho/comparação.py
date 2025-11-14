import numpy as np
import cv2
import time

IMG_PATH = "texture.jpg" #Path da imagem
img = np.array(cv2.imread(IMG_PATH))

kernel_sharpen = np.array([[0,-1,0],
                    [ -1, 5, -1],
                    [ 0, -1, 0]])

kernel_sobel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

kernel_blur = np.array([[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]],
                      dtype=np.float32)

kernel_high_boost = np.array([[ -1, -1, -1],
                        [ -1,  9, -1],
                        [ -1, -1, -1]])
kernel_edge = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],dtype=np.float32) # Edge detection
def kernel_sharpen_convolution():
    print("Kernel:kernel sharpen")

    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_sharpen)
    print(f"{(time.time() - start_time)} segundos para o opencv")

    cv2.imshow('kernel sharpen openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kernel_blur_convolution():
    print("Kernel:kernel blur")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_blur)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel blur openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kernel_sobel_convolution():
    print("Kernel:kernel sobel")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_sobel)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel sobel openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def kernel_high_boost_convolution():
    print("Kernel:kernel high boost")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_high_boost)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel outline openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kernel_edge_convolution():
    print("Kernel:kernel edge detection")
    
    start_time = time.time()
    img3 = cv2.filter2D(img,-1,kernel_edge)
    print(f"{(time.time() - start_time)} segundos para o opencv")
    
    cv2.imshow('kernel edge detection openCv',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

kernel_blur_convolution()
kernel_sharpen_convolution()
kernel_edge_convolution()
kernel_sobel_convolution()
kernel_high_boost_convolution()

