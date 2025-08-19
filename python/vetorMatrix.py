import numpy as np
from PIL import Image
from matplotlib import pyplot
IMG_PATH = "4.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))
mz = np.zeros((img.shape),dtype=img.dtype) 
mz[:,:,2] = img[:,:,2]
pyplot.imshow(mz)
pyplot.title('Canal Blue')
pyplot.show()