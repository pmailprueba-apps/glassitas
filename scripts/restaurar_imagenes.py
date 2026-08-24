import os, glob
from PIL import Image

dir_path = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
png_files = glob.glob(os.path.join(dir_path, "*.png"))

# El color original del fondo era aproximadamente (237, 237, 237)
bg_color = (237, 237, 237, 255)

for f in png_files:
    try:
        img = Image.open(f).convert("RGBA")
        width, height = img.size
        
        # Crear un fondo sólido del color original
        bg = Image.new("RGBA", (width, height), bg_color)
        
        # Pegar la imagen con transparencia encima del fondo sólido
        bg.alpha_composite(img)
        
        # Guardar como JPEG
        base = os.path.splitext(f)[0]
        out_path = base + ".jpeg"
        
        # Convertir a RGB para poder guardar como JPEG
        final_img = bg.convert("RGB")
        final_img.save(out_path, "JPEG", quality=100)
        
        print(f"Restaurada: {os.path.basename(out_path)}")
        
        # Borrar el PNG que estaba arruinado
        os.remove(f)
        
    except Exception as e:
        print(f"Error restaurando {f}: {e}")
