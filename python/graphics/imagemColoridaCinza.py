import numpy as np
from PIL import Image
from matplotlib import pyplot
IMG_PATH = "RGB-small.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))

x = (img[:,:,0] * 0.299 +
img[:,:,1] * 0.587 +
img[:,:,2] * 0.114)

pyplot.imshow(x,cmap="grey")
pyplot.title('Cinza')
pyplot.show()