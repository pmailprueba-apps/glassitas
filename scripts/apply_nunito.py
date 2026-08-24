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

    # 1. Update Google Fonts
    content = content.replace(
        'family=Dancing+Script:wght@400;700&family=Outfit:wght@300;400;500;600;700',
        'family=Dancing+Script:wght@400;700&family=Nunito:wght@300;400;500;600;700;800'
    )
    # Just in case there are stray Outfit links
    content = content.replace('family=Outfit:wght@300;400;500;600;700', 'family=Nunito:wght@300;400;500;600;700;800')

    # 2. Update Tailwind configuration
    content = content.replace('sans: [\'"Outfit"\', \'sans-serif\']', 'sans: [\'"Nunito"\', \'sans-serif\']')

    # 3. Upscale specific headings to compensate for Dancing Script optical size
    
    # Let's target the exact string in the javascript template literal first
    content = content.replace('<h3 class="text-xl font-serif font-bold text-deep-teal mb-2">${f.nombre}</h3>', '<h3 class="text-3xl font-serif font-bold text-deep-teal mb-2">${f.nombre}</h3>')
    content = content.replace('<h3 class="text-lg md:text-xl font-serif font-bold', '<h3 class="text-2xl md:text-4xl font-serif font-bold')
    
    # Other h3s that are text-2xl can become text-4xl
    content = content.replace('<h3 class="text-2xl font-serif', '<h3 class="text-4xl font-serif')
    
    # Fix the main titles H2 to text-5xl or text-6xl (they are already text-6xl, let's bump to 7xl maybe?)
    # "text-3xl md:text-6xl font-serif font-bold" -> "text-4xl md:text-7xl font-serif font-bold"
    content = content.replace('text-3xl md:text-6xl font-serif', 'text-5xl md:text-7xl font-serif')
    content = content.replace('text-3xl md:text-5xl font-serif', 'text-5xl md:text-7xl font-serif')

    # Update H1
    content = content.replace('text-6xl md:text-7xl font-serif', 'text-7xl md:text-8xl font-serif')
    
    # Remove old Outfit references in any remaining class strings if they exist
    content = content.replace('font-body', '') # if any

    with open(filepath, 'w') as f:
        f.write(content)

print("Fuentes aplicadas y escaladas.")
