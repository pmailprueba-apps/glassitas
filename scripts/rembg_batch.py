import os, glob
from rembg import remove
from PIL import Image

dir_path = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
jpeg_files = glob.glob(os.path.join(dir_path, "*.jpeg"))

for f in jpeg_files:
    try:
        print(f"Procesando con IA (rembg): {f}...")
        img = Image.open(f)
        out = remove(img)
        
        base = os.path.splitext(f)[0]
        out_path = base + ".png"
        out.save(out_path, "PNG")
        print(f"Fondo removido exitosamente: {os.path.basename(out_path)}")
    except Exception as e:
        print(f"Error procesando {f}: {e}")
