import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace tienda.html with nueva_web_pruebas/index.html
html = html.replace('href="tienda.html"', 'href="nueva_web_pruebas/index.html"')
html = html.replace('href="tienda.html#galeria"', 'href="nueva_web_pruebas/index.html#catalogo-galletas"')
html = html.replace('href="tienda.html#mayoreo"', 'href="nueva_web_pruebas/index.html#mayoreo"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Links updated!")
