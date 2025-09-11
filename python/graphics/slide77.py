import cv2
import numpy as np

canvas = cv2.imread("atitus1.png")

img_height,img_width,channels = canvas.shape

print(f"Altura {img_height}. Largura {img_width}. Canais {channels}.")

cv2.line(canvas,(50,0),(50,994),(0,0,255),1)
cv2.line(canvas,(100,0),(100,994),(0,0,255),1)
cv2.line(canvas,(150,0),(150,994),(0,0,255),1)

recorte = canvas[188:582,70:940]

recorte = recorte.copy()
cv2.line(recorte,(0,30),(869,30),(0,255,0),1)
cv2.line(recorte,(0,60),(869,60),(0,255,0),1)
cv2.line(recorte,(0,90),(869,90),(0,255,0),1)
cv2.line(recorte,(0,120),(869,120),(0,255,0),1)

cv2.line(recorte,(1,1),(866,393),(255,0,0),1)

recorte = cv2.flip(recorte, 1)

canvas[188:582,70:940] = recorte

cv2.imshow("image",canvas)
cv2.imwrite("desenho123.aitus.png",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()