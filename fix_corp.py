import re
import os

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

dest_dir = 'assets/productos/con_marco_blanco/galerias_con_marco'
for cat_id, folder_name in [('corporativo', 'corporativo'), ('institucion', 'institucion')]:
    folder_path = os.path.join(dest_dir, folder_name)
    if os.path.exists(folder_path):
        imgs = [f"../{dest_dir}/{folder_name}/{img}" for img in sorted(os.listdir(folder_path)) if img.endswith('.jpg')]
        if imgs:
            main_foto = imgs[0]
            # Replace REF_BASE + 'corporativo/img_1.jpg' with the actual baked image
            foto_regex = r"(id:\s*'" + cat_id + r"'.*?foto:\s*)[^,]+(,\s*fotos:)"
            html = re.sub(foto_regex, f"\\g<1>'{main_foto}'\\g<2>", html, flags=re.DOTALL)
            
            # Replace the fotos array
            fotos_regex = r"(id:\s*'" + cat_id + r"'.*?fotos:\s*\[)(.*?)(\])"
            imgs_str = ", ".join([f"'{img}'" for img in imgs])
            html = re.sub(fotos_regex, f"\\g<1>{imgs_str}\\g<3>", html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
