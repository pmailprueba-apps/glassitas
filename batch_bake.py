import os
from PIL import Image, ImageOps

source_dir = 'assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080'
dest_dir = 'assets/productos/optimizados/web_con_escaleta'
frame_path = 'assets/logo/escaletas/escaleta horizontal 2.png'

os.makedirs(dest_dir, exist_ok=True)
frame = Image.open(frame_path).convert("RGBA")

count = 0
for filename in os.listdir(source_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        base_img_path = os.path.join(source_dir, filename)
        base_img = Image.open(base_img_path).convert("RGBA")
        
        # Fit the base image to the frame size
        fitted_base = ImageOps.fit(base_img, frame.size, method=Image.Resampling.LANCZOS)
        
        # Paste the frame
        final = Image.alpha_composite(fitted_base, frame)
        
        # Save
        final = final.convert("RGB")
        # Save as jpg
        out_name = os.path.splitext(filename)[0] + '.jpg'
        out_path = os.path.join(dest_dir, out_name)
        final.save(out_path, quality=85)
        count += 1

print(f"Successfully baked {count} images to {dest_dir}")
