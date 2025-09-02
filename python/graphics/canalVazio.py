import numpy as np
from PIL import Image
from matplotlib import pyplot
IMG_PATH = "RGB-small.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))
matriz_vermelha = np.zeros((img.shape),dtype=img.dtype)
matriz_vermelha[:,:,0] = img[:,:,0]

matriz_verde = np.zeros((img.shape),dtype=img.dtype)
matriz_verde[:,:,1] = img[:,:,1] 

matriz_azul = np.zeros((img.shape),dtype=img.dtype)
matriz_azul[:,:,2] = img[:,:,2]

pyplot.imshow(matriz_vermelha)
pyplot.title('Canal Vermelho')
pyplot.show()

pyplot.imshow(matriz_verde)
pyplot.title('Canal Verde')
pyplot.show()

pyplot.imshow(matriz_azul)
pyplot.title('Canal Azul')
pyplot.show()