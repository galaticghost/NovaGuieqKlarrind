import numpy as np
from PIL import Image
from matplotlib import pyplot
IMG_PATH = "RGB-small.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))
img_red = img[:,:,0] # mudar o ultimo index para mudar a cor

pyplot.imshow(img_red,cmap='gray')
pyplot.title('Canal Vermelho')
pyplot.show()