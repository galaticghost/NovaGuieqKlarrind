import cv2
import numpy as np
from PIL import Image

canvas = np.zeros((600,800,3),dtype=np.uint8)
"""
x = 0
y = 0
while y != 700:
    cv2.line(canvas,(0,y),(800,y),(0,0,255),5)
    y += 100
while x != 900:
    cv2.line(canvas,(x,0),(x,600),(255,0,255),5)
    x += 100"""
# A
cv2.line(canvas,(100,500),(150,300),(255,0,0),5)
cv2.line(canvas,(150,300),(200,500),(255,0,0),5)
cv2.line(canvas,(100,400),(200,400),(255,0,0),5)

# R

cv2.rectangle(canvas,(200,300),(300,400),(255,0,0),5)
cv2.line(canvas,(200,400),(200,500),(255,0,0),5)
cv2.line(canvas,(200,400),(300,500),(255,0,0),5)

# T
cv2.line(canvas,(350,500),(350,300),(255,0,0),5)
cv2.line(canvas,(300,300),(400,300),(255,0,0),5)

# H
cv2.line(canvas,(400,500),(400,300),(255,0,0),5)
cv2.line(canvas,(500,500),(500,300),(255,0,0),5)
cv2.line(canvas,(400,400),(500,400),(255,0,0),5)

# U

cv2.line(canvas,(600,500),(600,300),(255,0,0),5)
cv2.line(canvas,(500,500),(500,300),(255,0,0),5)
cv2.line(canvas,(500,500),(600,500),(255,0,0),5)

# R
cv2.rectangle(canvas,(600,300),(700,400),(255,0,0),5)
cv2.line(canvas,(600,400),(700,500),(255,0,0),5)


cv2.imshow("Canvas",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()