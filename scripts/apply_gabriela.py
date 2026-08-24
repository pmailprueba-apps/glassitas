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

    # Replace Outfit with Gabriela
    content = content.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>',
        '<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Gabriela&display=swap" rel="stylesheet"/>'
    )
    
    content = content.replace(
        "sans: ['\"Outfit\"', 'sans-serif']",
        "sans: ['\"Gabriela\"', 'serif']"
    )

    with open(filepath, 'w') as f:
        f.write(content)

print("Fuente Gabriela aplicada.")
