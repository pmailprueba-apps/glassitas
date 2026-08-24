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

    # 1. Remove all injected <style> tags and weird font links
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="preconnect".*?>', '', content)
    content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]+" rel="stylesheet"[^>]*>', '', content)

    # 2. Add clean, standard font links (Material Symbols + Dancing Script + Outfit)
    standard_head_tags = """<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
"""
    head_end = content.find('</head>')
    if head_end != -1:
        content = content[:head_end] + standard_head_tags + content[head_end:]

    # 3. Clean Tailwind config
    tailwind_font_regex = re.compile(r'fontFamily:\s*{[^}]+}', re.DOTALL)
    clean_tailwind_fonts = """fontFamily: {
                    sans: ['"Outfit"', 'sans-serif'],
                    serif: ['"Dancing Script"', 'cursive']
                }"""
    content = tailwind_font_regex.sub(clean_tailwind_fonts, content)

    # 4. Clean body tag classes
    content = re.sub(r'<body class="[^"]*"', '<body class="font-sans bg-background text-on-surface text-base overflow-x-hidden selection:bg-terracotta/20"', content)

    # 5. Fix Hero H1 size to a clean, well-proportioned size (no overflow)
    content = re.sub(r'<h1 class="[^"]*"', '<h1 class="text-5xl md:text-6xl font-serif font-bold text-deep-teal mb-6 leading-tight"', content, count=1)

    # Clean redundant whitespace in class attributes
    content = re.sub(r'class="([^"]+)"', lambda m: 'class="' + ' '.join(m.group(1).split()) + '"', content)

    with open(filepath, 'w') as f:
        f.write(content)

print("Limpieza y estandarización completada.")
