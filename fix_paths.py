import os
import re

old_dir = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/con_marco_blanco/galerias con marco otra web'
new_dir = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/con_marco_blanco/galerias_con_marco'

# Rename directory
if os.path.exists(old_dir) and not os.path.exists(new_dir):
    os.rename(old_dir, new_dir)

# Update HTML
html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all occurrences of "galerias con marco otra web" with "galerias_con_marco"
html = html.replace('galerias con marco otra web', 'galerias_con_marco')

# Fix Hero Image to use Horizontal 1200x630
hero_old = '1_1_Cuadrado_1080x1080/31026464-65ed-4d2c-919d-c1ed6fb72773.jpg'
hero_new = '191_1_Horizontal_1200x630/31026464-65ed-4d2c-919d-c1ed6fb72773.jpg'
html = html.replace(hero_old, hero_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed spaces and hero image!")
