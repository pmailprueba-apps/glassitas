import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Revert hero image back to the square one requested by the user
old_hero_path = '../assets/productos/con_marco_blanco/galerias_con_marco/hero_horizontal.jpg'
new_hero_path = '../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/31026464-65ed-4d2c-919d-c1ed6fb72773.jpg'
html = html.replace(old_hero_path, new_hero_path)

# Fix the CSS size so it doesn't crop the square image
# Old container: <div class="relative rounded-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 2816/1536; max-height: 80vh;">
# New container: <div class="relative rounded-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 1/1; max-width: 600px; margin: 0 auto;">
old_container = '<div class="relative rounded-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 2816/1536; max-height: 80vh;">'
new_container = '<div class="relative rounded-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 1/1; max-width: 600px; margin: 0 auto;">'
html = html.replace(old_container, new_container)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
