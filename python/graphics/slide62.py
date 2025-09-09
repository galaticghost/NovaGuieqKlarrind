import cv2
import numpy as np

canvas = np.zeros((200,500,3),dtype=np.uint8)

cv2.line(canvas,(200,100),(400,150),(255,0,0),5)

cv2.imshow("Canvas",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()