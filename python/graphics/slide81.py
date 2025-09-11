import cv2
import numpy as np

img = cv2.imread("234.png") # Mude o nome da imagem se necessário
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low_red1 = np.array([0, 100, 100])
high_red1 = np.array([10, 255, 255])
low_red2 = np.array([170, 100, 100])
high_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, low_red1, high_red1)
mask2 = cv2.inRange(hsv, low_red2, high_red2)
mask = cv2.bitwise_or(mask1, mask2)

h, s, v = cv2.split(hsv)

h[mask > 0] = 60

hsv = cv2.merge([h, s, v])
img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("Imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()