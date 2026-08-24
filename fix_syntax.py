import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the backslashes from the ternary operators I accidentally injected
html = html.replace(r"\'", "'")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Syntax fixed!")
