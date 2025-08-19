import numpy as np
from PIL import Image

IMG_PATH = "atitus1-small.png" #Path da imagem
img = np.array(Image.open(IMG_PATH).convert("L"))

kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

img2 = np.zeros((img.shape))
