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
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
    body, p, a, span, div, h4, h5, h6, button, input, li { font-family: 'Lora', serif !important; }
    h1, h2, h3, .font-serif { font-family: 'Dancing Script', cursive !important; }
</style>
</head>
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove old font links and styles
    content = re.sub(r'<link rel="preconnect".*?</style>', '', content, flags=re.DOTALL)
    
    # Replace the tailwind config to Lora
    content = content.replace("sans: ['Quicksand', 'sans-serif']", "sans: ['Lora', 'serif']")

    content = content.replace('</head>', correct_head)

    with open(filepath, 'w') as f:
        f.write(content)

print("Cambiado a Lora.")
