import os
import numpy as np
from PIL import Image

uuid_dir = 'assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080'
raw_dir = 'contenido/referencia_fotogalletas/categorias'

def get_feature(path):
    img = Image.open(path).convert('L').resize((16, 16))
    return np.array(img, dtype=np.float32)

uuid_feats = {}
for filename in os.listdir(uuid_dir):
    if filename.endswith('.jpg'):
        path = os.path.join(uuid_dir, filename)
        uuid_feats[filename] = get_feature(path)

mapped = {}
for cat in os.listdir(raw_dir):
    cat_path = os.path.join(raw_dir, cat)
    if os.path.isdir(cat_path):
        mapped[cat] = []
        for filename in os.listdir(cat_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                raw_path = os.path.join(cat_path, filename)
                feat = get_feature(raw_path)
                
                best_match = None
                best_mse = float('inf')
                for u_name, u_feat in uuid_feats.items():
                    mse = np.mean((feat - u_feat) ** 2)
                    if mse < best_mse:
                        best_mse = mse
                        best_match = u_name
                
                # if best_mse < 2000:
                mapped[cat].append((filename, best_match, float(best_mse)))

import json
with open('mapping.json', 'w') as f:
    json.dump(mapped, f, indent=2)

for cat, matches in mapped.items():
    print(f"Category: {cat}")
    for m in matches[:2]:
        print(f"  {m[0]} -> {m[1]} (mse: {m[2]})")
