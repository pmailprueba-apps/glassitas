import re
import os

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace src="../${e.foto}" with src="${e.foto}"
html = html.replace('src="../${e.foto}"', 'src="${e.foto}"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
