import cv2
import numpy as np

img = cv2.imread("coins.png")
kernel = np.array([[0,1,0],[1,1,1],[0,1,1]],dtype=np.uint8)
kernel2 = np.ones((3,3),dtype=np.uint8)
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

img2 = cv2.erode(binary,kernel,iterations=1)
img3 = cv2.dilate(binary,kernel,iterations=1)

img4 = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel=kernel3)
img54 = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel=kernel3,)

#cv2.imshow("jdi",binary)
cv2.imshow("JAPMAN",img2)
cv2.imshow("XINA",img3)
cv2.imshow("KOIA?",img4)
cv2.imshow("SINGS?",img54)
cv2.waitKey(0)
cv2.destroyAllWindows()