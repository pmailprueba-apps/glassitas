import os

files = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

style_block = """
<style>
    body, p, a, span, div { font-family: 'Nunito', sans-serif !important; }
    h1, h2, h3, .font-serif { font-family: 'Dancing Script', cursive !important; }
</style>
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Add the style block right before </head> if it doesn't already exist
    if "<style>\n    body, p, a, span, div" not in content:
        content = content.replace('</head>', f'{style_block}\n</head>')

    # Remove the extra quotes in Tailwind config just in case
    content = content.replace('sans: [\'"Nunito"\', \'sans-serif\']', 'sans: [\'Nunito\', \'sans-serif\']')
    content = content.replace('serif: [\'"Dancing Script"\', \'cursive\']', 'serif: [\'Dancing Script\', \'cursive\']')

    with open(filepath, 'w') as f:
        f.write(content)

print("Estilos forzados inyectados.")
