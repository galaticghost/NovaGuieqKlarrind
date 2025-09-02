import numpy as np
import cv2
from PIL import Image

img = cv2.imread("2.png",cv2.COLOR_RGB2BGR)

kernel = np.ones((5, 5), np.float32)/25

img2 = cv2.filter2D(img,-1,kernel)

kernel2 = np.array([[-1,-1,-1],
                    [ 0, 0, 0],
                    [ 1, 1, 1]])

img3 = cv2.filter2D(img,-1,kernel2)

kernel_blur = np.ones((3,3), np.float32) / 9

img4 = cv2.filter2D(img,-1,kernel_blur)

kernel_h = np.array([[1, 1, 1], 
                     [0, 0, 0], 
                     [-1, -1, -1]])

img5 = cv2.filter2D(img,-1,kernel_h)

kernel_v = np.transpose(kernel_h)
print(kernel_v)
img6 = cv2.filter2D(img,-1,kernel_v)
"""cv2.imshow('4',img)
cv2.imshow('45',img2)
cv2.imshow('455',img3)
cv2.imshow('1455',img4)"""
cv2.imshow('Horizontal',img5)
cv2.imshow('Vertical',img6)
cv2.waitKey(0)
cv2.destroyAllWindows()