import re
import os

dest_dir = 'assets/productos/con_marco_blanco/galerias con marco otra web'

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Map folder names to EVENTOS ids
cat_map = {
    'baby_shower': 'baby-shower',
    'bautizo': 'bautizo',
    'boda': 'boda',
    'comunion': 'comunion',
    'cumpleanos': 'cumpleanos',
    'graduacion': 'graduacion',
    'corporativo': 'logotipos',
    'institucion': 'institucionales',
    'xv': 'xv'
}

for folder_name, cat_id in cat_map.items():
    folder_path = os.path.join(dest_dir, folder_name)
    if not os.path.exists(folder_path):
        continue
        
    imgs = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.jpg'):
            imgs.append(f"../{dest_dir}/{folder_name}/{filename}")
            
    if not imgs:
        continue
        
    main_foto = imgs[0]
    
    # 1. Replace main foto
    # id: 'baby-shower', nombre: 'Galletas de Baby Shower', ico: '🍼',
    # foto: REF_BASE + 'baby_shower/img_1.jpg',
    foto_regex = r"(id:\s*'" + cat_id + r"'.*?foto:\s*)[^,]+(,\s*fotos:)"
    
    def replacer_foto(match):
        return f"{match.group(1)}'{main_foto}'{match.group(2)}"
        
    html = re.sub(foto_regex, replacer_foto, html, flags=re.DOTALL)
    
    # 2. Replace fotos array
    # fotos: ['...', '...'],
    fotos_regex = r"(id:\s*'" + cat_id + r"'.*?fotos:\s*\[)(.*?)(\])"
    
    def replacer_fotos(match):
        imgs_str = ", ".join([f"'{img}'" for img in imgs])
        return f"{match.group(1)}{imgs_str}{match.group(3)}"
        
    html = re.sub(fotos_regex, replacer_fotos, html, flags=re.DOTALL)

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML successfully fixed!")
