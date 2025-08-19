import numpy as np
from PIL import Image
from matplotlib import pyplot
IMG_PATH = "RGB-small.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))
matriz_zero = np.zeros((img.shape),dtype=img.dtype)
matriz_zero[:,:,0] = img[:,:,0] # mudar o ultimo index para mudar a cor

pyplot.imshow(matriz_zero)
pyplot.title('Canal Vermelho')
pyplot.show()