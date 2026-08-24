import re
import os

files = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

style_block = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Quicksand:wght@300;400;500;600;700&display=swap');
body, p, a, span, div, h4, h5, h6, button, input, li { font-family: 'Quicksand', sans-serif !important; }
h1, h2, h3, .font-serif { font-family: 'Dancing Script', cursive !important; }
</style>
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Clean old link tags for fonts to avoid conflicts
    content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=(Dancing|Quicksand|Nunito|Outfit)[^"]+" rel="stylesheet"/>', '', content)
    
    # 2. Inject the ultimate style block right before </head>
    # First remove any existing style blocks we might have injected before (just in case they are lingering)
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    head_end = content.find('</head>')
    if head_end != -1:
        content = content[:head_end] + f"\n{style_block}\n" + content[head_end:]

    # 3. Fix the overflowing H1 title (reduce size)
    content = content.replace('text-7xl md:text-8xl font-serif', 'text-5xl md:text-6xl font-serif')
    content = content.replace('text-7xl md:text-8xl', 'text-5xl md:text-6xl')
    
    # Also adjust H2 a bit if they were too huge
    content = content.replace('text-5xl md:text-7xl', 'text-4xl md:text-5xl')

    with open(filepath, 'w') as f:
        f.write(content)

print("Fix definitivo aplicado.")
