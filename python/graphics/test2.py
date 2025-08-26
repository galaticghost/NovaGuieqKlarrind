import numpy as np
import cv2

canvas = np.zeros((200, 500, 3), dtype=np.uint8)

triangle_pts = np.array([[50, 150], [100, 50], [150, 150]])

cv2.polylines(canvas, [triangle_pts], True, [255, 0, 0], 2)

translation_vector = np.array([200, -25], dtype=np.int32)

translated_pts = triangle_pts + translation_vector

cv2.polylines(canvas, [translated_pts], True, [0, 255, 0], 2)
cv2.imshow("Triangulos", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()