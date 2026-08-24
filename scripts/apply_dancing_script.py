import os
import re

files_to_update = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

font_link_regex = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]+" rel="stylesheet"/>')
new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>'

tailwind_regex = re.compile(r'fontFamily:\s*{[^}]+}', re.DOTALL)
new_tailwind = """fontFamily: {
                        sans: ['"Outfit"', 'sans-serif'],
                        serif: ['"Dancing Script"', 'cursive']
                    }"""

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Update Google Fonts
    if font_link_regex.search(content):
        content = font_link_regex.sub(new_font_link, content)
    else:
        # Fallback if regex misses
        content = content.replace('family=Plus+Jakarta+Sans:wght@400;500;600&family=Outfit:wght@300;400;600;700', 'family=Dancing+Script:wght@400;700&family=Outfit:wght@300;400;500;600;700')

    # Update Tailwind config
    content = tailwind_regex.sub(new_tailwind, content)

    # Make H1, H2, H3 use font-serif font-bold and increase size
    # H1
    content = re.sub(r'(<h1[^>]*class="[^"]*)font-serif-mobile md:text-6xl([^"]*")', r'\1md:text-7xl\2', content)
    content = re.sub(r'(<h1[^>]*class="[^"]*)(text-\d+xl)([^"]*")', lambda m: m.group(1) + 'text-7xl font-serif font-bold' + m.group(3).replace('font-serif', '').replace('font-bold', ''), content)
    
    # H2
    content = re.sub(r'(<h2[^>]*class="[^"]*)(text-\d+xl|text-lg|text-xl)([^"]*")', lambda m: m.group(1) + m.group(2) + ' font-serif font-bold' + m.group(3).replace('font-serif', '').replace('font-bold', ''), content)
    content = content.replace('md:text-5xl font-serif font-bold', 'md:text-6xl font-serif font-bold')
    
    # H3
    content = re.sub(r'(<h3[^>]*class="[^"]*)(text-\d+xl|text-lg|text-xl)([^"]*")', lambda m: m.group(1) + m.group(2) + ' font-serif font-bold' + m.group(3).replace('font-serif', '').replace('font-bold', ''), content)

    # Clean up double classes
    content = content.replace('font-serif font-serif', 'font-serif')
    content = content.replace('font-bold font-bold', 'font-bold')

    with open(filepath, 'w') as f:
        f.write(content)

print("Actualizado.")
