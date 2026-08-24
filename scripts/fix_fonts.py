import re
import os

files = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Clean up duplicate links. 
    # There are 3 identical links now. We only need ONE Dancing Script + Outfit, and ONE Material Symbols.
    dancing_link = '<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'
    material_link = '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>'
    
    # Remove all dancing script links temporarily
    content = content.replace(dancing_link, '')
    # Add them back carefully in the head
    head_end = content.find('</head>')
    if head_end != -1:
        links = f"\n{material_link}\n{dancing_link}\n"
        content = content[:head_end] + links + content[head_end:]

    # 2. Fix duplicate font-bold
    content = content.replace('font-bold font-bold', 'font-bold')
    content = content.replace('font-serif font-bold font-semibold', 'font-serif font-bold')
    content = content.replace('text-6xl font-bold md:text-7xl font-serif', 'text-6xl md:text-7xl font-serif font-bold')
    content = re.sub(r' +', ' ', content) # clean up spaces in classes

    # 3. Add font-serif font-bold to h3 where it missed (line 755)
    content = content.replace('<h3>${f.nombre}</h3>', '<h3 class="text-xl font-serif font-bold text-deep-teal mb-2">${f.nombre}</h3>')

    with open(filepath, 'w') as f:
        f.write(content)

print("Arreglado.")
