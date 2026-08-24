import os
from PIL import Image, ImageOps
from pathlib import Path

frame_path = 'assets/logo/escaletas/escaleta horizontal 2.png'
in_dir = Path('contenido/referencia_fotogalletas/categorias')
out_dir = Path('contenido/referencia_fotogalletas/categorias_con_marco')

if not out_dir.exists():
    out_dir.mkdir(parents=True)

try:
    frame = Image.open(frame_path).convert("RGBA")
except Exception as e:
    print(f"Error loading frame: {e}")
    exit(1)

W, H = frame.size
count = 0

for root, dirs, files in os.walk(in_dir):
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            in_path = Path(root) / f
            
            # Preserve directory structure
            rel_path = in_path.relative_to(in_dir)
            out_path = out_dir / rel_path
            
            if not out_path.parent.exists():
                out_path.parent.mkdir(parents=True)
                
            try:
                img = Image.open(in_path).convert("RGBA")
                img_fitted = ImageOps.fit(img, (W, H), method=Image.Resampling.LANCZOS)
                
                final = Image.new("RGBA", (W, H))
                final.paste(img_fitted, (0, 0))
                final.paste(frame, (0, 0), frame)
                
                final_rgb = final.convert("RGB")
                
                out_path_jpg = out_path.with_suffix('.jpg')
                final_rgb.save(out_path_jpg, quality=85)
                count += 1
            except Exception as e:
                print(f"Error processing {in_path}: {e}")

print(f"Successfully baked frames into {count} images.")
