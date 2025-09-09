import numpy as np
import cv2

img = cv2.imread("easy2.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)
opened = cv2.dilate(eroded, kernel, iterations=1)
dilated = cv2.dilate(opened, kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)


cv2.imshow("g2a",hierarchy)
cv2.imshow("g3a",dilated)


cv2.waitKey(0)
cv2.destroyAllWindows()

