import numpy as np
from PIL import Image
IMG_PATH = "RGB-small.png"
img = np.array(Image.open(IMG_PATH).convert("RGB"))

print(f"Resolução: {img.shape}")
print(f"Data type: {img.dtype}")
print("Vermelho")
print(img[:15,:15,0])
print("Verde")
print(img[:15,:15,1])
print("Azul")
print(img[:15,:15,2])
