import re
import os

files = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

bg_div = '\n<!-- Faint Background Image -->\n<div class="fixed inset-0 z-[-1] bg-[url(\'../assets/background.jpeg\')] bg-cover bg-center bg-no-repeat opacity-[0.20] pointer-events-none"></div>\n'

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Change body background color to off-white and add relative
    content = content.replace('bg-background text-on-surface', 'bg-[#FDFBF7] text-on-surface')
    if 'relative' not in content.split('<body')[1].split('>')[0]:
         content = content.replace('overflow-x-hidden', 'overflow-x-hidden relative')

    # Inject the fixed background div if not already there
    if '<!-- Faint Background Image -->' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1' + bg_div, content, count=1)

    with open(filepath, 'w') as f:
        f.write(content)

print("Background modificado a imagen tenue.")
