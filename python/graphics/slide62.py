import cv2
import numpy as np
from random import randint

canvas = np.zeros((200,500,3),dtype=np.uint8)

cv2.line(canvas,(200,100),(400,150),(255,0,0),5)

def getCoeficientes(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - m * p1[0]
    return m,b

m,b = getCoeficientes((200,100),(400,150))

def drawline(x):
    y = m*x + b
    y = int(y)
    cv2.line(canvas,(x,y),(x,y),(127,127,127),5)

for _ in range(0,10):
    x = randint(200,400)
    drawline(x)

cv2.imshow("Canvas",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()