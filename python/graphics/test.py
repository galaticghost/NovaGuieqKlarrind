import cv2
import numpy as np
from PIL import Image

img2 = np.array(Image.open("3.jpg"))
#img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
img = np.ones((800,600,3),dtype=np.uint8) * 255
cv2.line(img2,(0,0),(550,750),(255,0,0),5)
cv2.imshow('Bola2',img)
cv2.imshow("vamp",img2)


cv2.waitKey(0)
cv2.destroyAllWindows()