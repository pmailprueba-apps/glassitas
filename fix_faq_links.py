import re
import os

root_dir = '/Volumes/MiDisco1TB/Proyectos/44-glassitas'
nueva_web = os.path.join(root_dir, 'nueva_web_pruebas')

# 1. Copy the FAQ into the nueva_web_pruebas folder
with open(os.path.join(root_dir, 'preguntas-frecuentes.html'), 'r', encoding='utf-8') as f:
    faq_html = f.read()

# Fix links in FAQ to match index.html's path level
# Since index.html uses `../assets/`, FAQ in the same folder will also use `../assets/`
# In the original FAQ it was probably `assets/` or `../assets/` depending on who edited it.
# Wait, if previous agent made it identical to index.html, it already has `../assets/`.
# Let's fix the hrefs to itself and index.html:
faq_html = faq_html.replace('href="../preguntas-frecuentes.html"', 'href="preguntas-frecuentes.html"')
faq_html = faq_html.replace('href="index.html"', 'href="index.html"')
faq_html = faq_html.replace('href="../index.html"', 'href="index.html"')

with open(os.path.join(nueva_web, 'preguntas-frecuentes.html'), 'w', encoding='utf-8') as f:
    f.write(faq_html)

# 2. Fix the links in index.html to point to the local faq
with open(os.path.join(nueva_web, 'index.html'), 'r', encoding='utf-8') as f:
    idx_html = f.read()

idx_html = idx_html.replace('href="../preguntas-frecuentes.html"', 'href="preguntas-frecuentes.html"')
idx_html = idx_html.replace('href="../index.html"', 'href="index.html"')

with open(os.path.join(nueva_web, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(idx_html)

print("FAQ moved and links fixed!")
