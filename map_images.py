import os
import imagehash
from PIL import Image

uuid_dir = 'assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080'
raw_dir = 'contenido/referencia_fotogalletas/categorias'

uuid_hashes = {}
for filename in os.listdir(uuid_dir):
    if filename.endswith('.jpg'):
        path = os.path.join(uuid_dir, filename)
        # Using a crop or resize might be needed, but phash is somewhat robust
        img = Image.open(path).convert('RGB')
        h = imagehash.phash(img)
        uuid_hashes[filename] = h

mapped = {}
for cat in os.listdir(raw_dir):
    cat_path = os.path.join(raw_dir, cat)
    if os.path.isdir(cat_path):
        mapped[cat] = []
        for filename in os.listdir(cat_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                raw_path = os.path.join(cat_path, filename)
                img = Image.open(raw_path).convert('RGB')
                h = imagehash.phash(img)
                
                # Find closest match in UUIDs
                best_match = None
                best_dist = float('inf')
                for u_name, u_hash in uuid_hashes.items():
                    dist = h - u_hash
                    if dist < best_dist:
                        best_dist = dist
                        best_match = u_name
                
                if best_dist < 25: # threshold
                    mapped[cat].append((filename, best_match, best_dist))

for cat, matches in mapped.items():
    print(f"Category: {cat}")
    for m in matches[:2]:
        print(f"  {m[0]} -> {m[1]} (dist: {m[2]})")
