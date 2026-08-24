from PIL import Image
import os

img_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0047ac48-1662-4bcc-88b1-e547cdc92e8e.jpg'
img = Image.open(img_path)
print(f"Size: {img.size}")
