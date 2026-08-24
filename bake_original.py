import os
import shutil
from PIL import Image, ImageOps

raw_dir = 'contenido/referencia_fotogalletas/categorias'
dest_dir = 'assets/productos/con_marco_blanco/galerias con marco otra web'
frame_path = 'assets/logo/escaletas/escaleta insta.png'

# Delete old UUID baked files
if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
os.makedirs(dest_dir, exist_ok=True)

frame = Image.open(frame_path).convert("RGBA")

baked_files = {}

count = 0
for cat in os.listdir(raw_dir):
    cat_path = os.path.join(raw_dir, cat)
    if os.path.isdir(cat_path):
        os.makedirs(os.path.join(dest_dir, cat), exist_ok=True)
        baked_files[cat] = []
        for filename in os.listdir(cat_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                raw_path = os.path.join(cat_path, filename)
                base_img = Image.open(raw_path).convert("RGBA")
                
                # PAD the base image to the frame size (don't crop!)
                # Color white (255,255,255,255)
                fitted_base = ImageOps.pad(base_img, frame.size, method=Image.Resampling.LANCZOS, color=(255, 255, 255, 255))
                
                final = Image.alpha_composite(fitted_base, frame)
                final = final.convert("RGB")
                
                out_name = os.path.splitext(filename)[0] + '.jpg'
                out_path = os.path.join(dest_dir, cat, out_name)
                final.save(out_path, quality=90)
                
                # Store relative path for HTML
                rel_path = f"../assets/productos/con_marco_blanco/galerias con marco otra web/{cat}/{out_name}"
                baked_files[cat].append(rel_path)
                count += 1

print(f"Procesadas {count} imagenes ORIGINALES en {dest_dir}")

# Update HTML
import re
with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# For each category in EVENTOS, we replace its imagenes list
import ast
eventos_match = re.search(r'const\s+EVENTOS\s*=\s*(\[.*?\]);', html, re.DOTALL)
if eventos_match:
    # Safely evaluating is tricky, but we can just regex replace the imagenes array for each category ID
    for cat, imgs in baked_files.items():
        # find the block for this category
        cat_regex = r"id:\s*'" + cat + r"'.*?imagenes:\s*\[(.*?)\]"
        # We need a function to replace only the images array
        
        def replacer(match):
            imgs_str = ",\n        ".join([f"'{img}'" for img in imgs])
            return match.group(0).replace(match.group(1), "\n        " + imgs_str + "\n      ")
            
        html = re.sub(cat_regex, replacer, html, flags=re.DOTALL)

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("HTML Actualizado con las fotos de impresion reales!")
