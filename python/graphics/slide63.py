import cv2
import numpy as np

canvas = np.zeros((800,200,3),dtype=np.uint8)

cv2.circle(canvas,center=(100,400),radius=50,color=(0,0,255),thickness=-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(10000)

cv2.circle(canvas,center=(100,400),radius=50,color=(0,255,255),thickness=-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(10000)

cv2.circle(canvas,center=(100,400),radius=50,color=(0,255,0),thickness=-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(10000)

cv2.destroyAllWindows()