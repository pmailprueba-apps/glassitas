from PIL import Image
img = Image.open("/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas/prueba_exterior_blanco.png")
w, h = img.size
print(f"Center pixel: {img.getpixel((w//2, h//2))}")
