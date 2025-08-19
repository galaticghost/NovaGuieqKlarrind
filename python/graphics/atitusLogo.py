import numpy as np
from PIL import Image

IMG_PATH = "atitus1-small.png" #Path da imagem
img = np.array(Image.open(IMG_PATH).convert("L"))

print(f"Resolução: {img.shape}")
print(img[:15,:15])