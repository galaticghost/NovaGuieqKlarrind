import cv2
import numpy as np
from PIL import Image

canvas = np.zeros((600,800,3),dtype=np.uint8)

x = 0
y = 0
while y != 700:
    cv2.line(canvas,(0,y),(800,y),(0,0,255),5)
    y += 100
while x != 900:
    cv2.line(canvas,(x,0),(x,600),(255,0,255),5)
    x += 100
# A
cv2.line(canvas,(70,500),(150,300),(255,0,0),5)
cv2.line(canvas,(150,300),(230,500),(255,0,0),5)
cv2.line(canvas,(70,400),(230,400),(255,0,0),5)

# R

cv2.rectangle(canvas,(200,280),(300,380),(255,0,0),5)
cv2.line(canvas,(200,380),(200,480),(255,0,0),5)
cv2.line(canvas,(200,380),(300,480),(255,0,0),5)

# T
cv2.line(canvas,(320,500),(380,300),(255,0,0),5)
cv2.line(canvas,(330,270),(430,330),(255,0,0),5)

# H
cv2.line(canvas,(400,480),(400,280),(255,0,0),5)
cv2.line(canvas,(500,480),(500,280),(255,0,0),5)
cv2.line(canvas,(400,380),(500,380),(255,0,0),5)

# U

cv2.line(canvas,(600,500),(600,300),(255,0,0),5)
cv2.line(canvas,(500,500),(500,300),(255,0,0),5)
cv2.line(canvas,(500,500),(600,500),(255,0,0),5)

# R
cv2.rectangle(canvas,(650,250),(700,380),(255,0,0),5)
cv2.line(canvas,(600,380),(700,480),(255,0,0),5)

cv2.imshow("Canvas",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()