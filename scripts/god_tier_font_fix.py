import re
import os

files = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

correct_head = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Quicksand:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    body, p, a, span, div, h4, h5, h6, button, input, li { font-family: 'Quicksand', sans-serif !important; }
    h1, h2, h3, .font-serif { font-family: 'Dancing Script', cursive !important; }
</style>
</head>
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Clean completely any old styles or links we injected
    content = re.sub(r'<style>\s*@import.*?cursive !important; \s*}\s*</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=(Dancing|Quicksand|Nunito|Outfit)[^"]+" rel="stylesheet"/>', '', content)
    content = re.sub(r'<link rel="preconnect"[^>]+>', '', content)

    # Inject the god tier block right at </head>
    content = content.replace('</head>', correct_head)

    with open(filepath, 'w') as f:
        f.write(content)

print("God tier fix aplicado.")
