import os
import glob
from PIL import Image

input_dir = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos"
output_base = os.path.join(input_dir, "optimizados")

sizes = {
    "1_1_Cuadrado_1080x1080": (1080, 1080),
    "4_5_Vertical_1080x1350": (1080, 1350),
    "9_16_Historias_1080x1920": (1080, 1920),
    "191_1_Horizontal_1200x630": (1200, 630)
}

# Crear carpetas
for folder in sizes.keys():
    os.makedirs(os.path.join(output_base, folder), exist_ok=True)

valid_exts = ("*.jpg", "*.jpeg", "*.png")
files = []
for ext in valid_exts:
    files.extend(glob.glob(os.path.join(input_dir, ext)))
    files.extend(glob.glob(os.path.join(input_dir, ext.upper())))

if not files:
    print(f"No se encontraron imágenes válidas en {input_dir}")
else:
    for f in set(files):
        try:
            img = Image.open(f)
            base_name = os.path.basename(f)
            print(f"Procesando: {base_name}")
            
            for folder, (t_w, t_h) in sizes.items():
                # Center crop and resize
                img_ratio = img.width / img.height
                target_ratio = t_w / t_h
                
                if img_ratio > target_ratio:
                    new_w = int(img.height * target_ratio)
                    left = (img.width - new_w) / 2
                    cropped = img.crop((left, 0, left + new_w, img.height))
                else:
                    new_h = int(img.width / target_ratio)
                    top = (img.height - new_h) / 2
                    cropped = img.crop((0, top, img.width, top + new_h))
                
                final_img = cropped.resize((t_w, t_h), Image.LANCZOS)
                
                if final_img.mode in ("RGBA", "P"):
                    final_img = final_img.convert("RGB")
                
                out_path = os.path.join(output_base, folder, f"{os.path.splitext(base_name)[0]}.jpg")
                final_img.save(out_path, "JPEG", quality=95)
        except Exception as e:
            print(f"Error con {f}: {e}")
                
    print(f"\n¡Todas las imágenes fueron recortadas y organizadas en {output_base}!")
