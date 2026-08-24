import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/preguntas-frecuentes.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix all the broken links that duplicate the folder name
html = html.replace('href="nueva_web_pruebas/index.html', 'href="index.html')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Links cleaned up in FAQs!")
