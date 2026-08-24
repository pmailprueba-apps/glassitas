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

    # 1. Remove the forced style block
    style_regex = re.compile(r'<style>\s*body, p, a, span, div { font-family: [^<]+</style>', re.DOTALL)
    content = style_regex.sub('', content)

    # 2. Fix Google Fonts links by splitting them
    # First remove any existing font links (except Material Symbols)
    content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=(Dancing|Nunito|Outfit)[^"]+" rel="stylesheet"/>', '', content)
    
    # Insert new separate links before </head>
    dancing_link = '<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet"/>'
    quicksand_link = '<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'
    
    head_end = content.find('</head>')
    if head_end != -1:
        content = content[:head_end] + f"\n{dancing_link}\n{quicksand_link}\n" + content[head_end:]

    # 3. Update Tailwind config to Quicksand
    content = content.replace("sans: ['Nunito', 'sans-serif']", "sans: ['Quicksand', 'sans-serif']")
    content = content.replace("sans: ['\"Nunito\"', 'sans-serif']", "sans: ['Quicksand', 'sans-serif']")
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Fuentes Quicksand y Dancing separadas aplicadas.")
