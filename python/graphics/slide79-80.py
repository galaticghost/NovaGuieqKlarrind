import cv2
import numpy as np


img = cv2.imread("opencvlogo.png")
# --- Coordenadas do quadrado azul ---
x1, y1 = 178, 156
x2, y2 = 322, 300

# 1. Recortar o quadrado azul da imagem original
roi = img[y1:y2, x1:x2]
(h, w) = roi.shape[:2]
center = (w // 2, h // 2)

# 2. Criar a matriz de rotação e rotacionar 45°
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(roi, M, (w, h))

# 3. Criar máscara para o círculo (onde é diferente de preto)
gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# 4. Remover a área antiga da imagem original
roi_original = img[y1:y2, x1:x2]
background = cv2.bitwise_and(roi_original, roi_original, mask=cv2.bitwise_not(mask))

# 5. Colar a parte rotacionada por cima
final_roi = cv2.add(background, rotated)

# 6. Substituir de volta na imagem original
img[y1:y2, x1:x2] = final_roi

# 7. Mostrar resultado
cv2.imshow("Imagem com azul rotacionado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
