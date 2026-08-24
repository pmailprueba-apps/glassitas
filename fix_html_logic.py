import re

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the renderEventos logic for e.foto (Cover)
# Old: <img src="${e.has_frame ? '' : '../'}${e.has_frame ? e.foto : REF_BASE + e.foto}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy">
# New: <img src="${e.foto}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy">
old_img_src = r'<img src="\$\{e\.has_frame \? \'\' : \'\.\./\'\}\$\{e\.has_frame \? e\.foto : REF_BASE \+ e\.foto\}"'
new_img_src = r'<img src="${e.foto}"'
html = re.sub(old_img_src, new_img_src, html)

# Fix the renderEventos logic for e.fotos (Gallery)
# Old: const ejemplos = (e.fotos || []).map(f => '../' + REF_BASE + f);
# New: const ejemplos = (e.fotos || []);
old_fotos_map = r"const ejemplos = \(e\.fotos \|\| \[\]\)\.map\(f => '\.\./' \+ REF_BASE \+ f\);"
new_fotos_map = r"const ejemplos = (e.fotos || []);"
html = re.sub(old_fotos_map, new_fotos_map, html)

# Now fix corporativo and institucion in EVENTOS to just point to the baked images!
# For Logotipos (corporativo)
import os
dest_dir = 'assets/productos/con_marco_blanco/galerias_con_marco'
for cat_id, folder_name in [('logotipos', 'corporativo'), ('institucionales', 'institucion')]:
    folder_path = os.path.join(dest_dir, folder_name)
    if os.path.exists(folder_path):
        imgs = [f"../{dest_dir}/{folder_name}/{img}" for img in sorted(os.listdir(folder_path)) if img.endswith('.jpg')]
        if imgs:
            main_foto = imgs[0]
            # fix main foto
            foto_regex = r"(id:\s*'" + cat_id + r"'.*?foto:\s*)[^,]+(,\s*fotos:)"
            html = re.sub(foto_regex, f"\\g<1>'{main_foto}'\\g<2>", html, flags=re.DOTALL)
            
            # fix fotos array
            fotos_regex = r"(id:\s*'" + cat_id + r"'.*?fotos:\s*\[)(.*?)(\])"
            imgs_str = ", ".join([f"'{img}'" for img in imgs])
            html = re.sub(fotos_regex, f"\\g<1>{imgs_str}\\g<3>", html, flags=re.DOTALL)

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML logic fixed!")
