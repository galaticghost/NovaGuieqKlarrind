import cv2
import numpy as np

img = cv2.imread("easy.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

cv2.imshow("jdi",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()