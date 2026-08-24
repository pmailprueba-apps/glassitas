import os, glob
from PIL import Image

dir_path = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
png_files = glob.glob(os.path.join(dir_path, "*.png"))

def remove_white_bg(img_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()

    newData = []
    # Umbral de tolerancia para el blanco (puede que tenga un ligero gris/beige)
    threshold = 240
    for item in datas:
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Hacerlo completamente transparente
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(img_path, "PNG")
    print(f"Fondo quitado a: {os.path.basename(img_path)}")

if not png_files:
    print("No se encontraron PNGs.")
else:
    for f in png_files:
        try:
            remove_white_bg(f)
        except Exception as e:
            print(f"Error procesando {f}: {e}")
