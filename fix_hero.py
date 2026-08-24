import re
import os
import shutil

# Move the test_horizontal.jpg (which is the hero with the horizontal frame) to a permanent spot
src_test = 'test_horizontal.jpg'
dest_img = 'assets/productos/con_marco_blanco/galerias_con_marco/hero_horizontal.jpg'
shutil.copy(src_test, dest_dir := dest_img)

# Update HTML
html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero image path
old_hero_path = '../assets/productos/con_marco_blanco/191_1_Horizontal_1200x630/31026464-65ed-4d2c-919d-c1ed6fb72773.jpg'
new_hero_path = '../assets/productos/con_marco_blanco/galerias_con_marco/hero_horizontal.jpg'
html = html.replace(old_hero_path, new_hero_path)

# Fix the hero container height so it doesn't zoom/crop the frame
# Old: <div class="relative rounded-lg overflow-hidden ambient-shadow h-[400px] md:h-[600px] w-full">
# New: <div class="relative rounded-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 2816/1536;">
old_container = '<div class="relative rounded-lg overflow-hidden ambient-shadow h-[400px] md:h-[600px] w-full">'
new_container = '<div class="relative rounded-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 2816/1536; max-height: 80vh;">'
html = html.replace(old_container, new_container)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Hero image and container aspect ratio fixed!")
