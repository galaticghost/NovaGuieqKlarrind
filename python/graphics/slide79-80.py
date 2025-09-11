import cv2
import numpy as np

img = cv2.imread("opencvlogo.png")

canvas = img.copy()

print('Resolucao da imagem (Altura x Largura x Canais):', canvas.shape)
print('Data type da imagem:', canvas.dtype)

blue = canvas[143:300,170:333].copy()

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

blue = rotate_image(blue,57)

altura, largura, _ = blue.shape

for i in range(altura):
    for j in range(largura):
        if blue[i,j].sum() != 414:
            blue[i,j] = [255,255,255]

canvas[143:300,170:333] = blue

cv2.imshow("image",canvas)
#cv2.imwrite("desenho123.opencv.png",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()