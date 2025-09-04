import numpy as np
from PIL import Image
from matplotlib import pyplot
IMG_PATH = "RGB-small.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))
img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2] 
pyplot.imshow(img_red,cmap='gray')
pyplot.title('Canal Vermelho')
pyplot.show()

pyplot.imshow(img_green,cmap='gray')
pyplot.title('Canal Verde')
pyplot.show()

pyplot.imshow(img_blue,cmap='gray')
pyplot.title('Canal Azul')
pyplot.show()