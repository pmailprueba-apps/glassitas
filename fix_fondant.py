import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken paths in the EVENTOS array
html = html.replace('../assets/productos/con_marco_blanco/0047ac48', '../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0047ac48')
html = html.replace('../assets/productos/con_marco_blanco/02ccee75', '../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/02ccee75')
html = html.replace('../assets/productos/con_marco_blanco/031d1e47', '../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/031d1e47')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fondant images fixed!")
