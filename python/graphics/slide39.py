import cv2
import numpy as np

canvas = np.ones((400,600,3),dtype=np.uint8) * 255

cv2.circle(canvas,center=(300,200),radius=50,color=(0,0,255),thickness=-1)

cv2.line(canvas,(250,300),(300,100),(255,0,0),5)
cv2.line(canvas,(300,100),(350,300),(255,0,0),5)
cv2.line(canvas,(250,200),(350,200),(255,0,0),5)

cv2.imshow("Canvas",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()