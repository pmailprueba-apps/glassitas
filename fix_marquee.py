import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the broken image path in the marquee
html = html.replace('src="../assets/productos/con_marco_blanco/0', 'src="../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0')
html = html.replace("openLightbox('../assets/productos/con_marco_blanco/0", "openLightbox('../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Marquee images fixed!")
