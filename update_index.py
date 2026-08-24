import re
import os

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 3. Update REF_BASE
html = html.replace("const REF_BASE = 'contenido/referencia_fotogalletas/categorias/';", "const REF_BASE = 'contenido/referencia_fotogalletas/categorias_con_marco/';")

# 2. Add "Galletas de Fondant Personalizadas" category
# We need to prepend it to EVENTOS array.
# First, let's get the list of files in con_marco_blanco/191_1_Horizontal_1200x630/
fondant_dir = 'assets/productos/con_marco_blanco/191_1_Horizontal_1200x630'
files = []
if os.path.exists(fondant_dir):
    files = [f for f in os.listdir(fondant_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    files = sorted(files)

# We want only the first 8 photos for the array (or all of them, but 8 is enough).
fondant_fotos = files[:8]
# Format them into JS strings.
# Wait, REF_BASE points to 'contenido/...'. But fondant images are in 'assets/productos/...'.
# So the foto and fotos for Fondant must override REF_BASE or include the full path relative to html.
fondant_js_fotos = []
for f in fondant_fotos:
    fondant_js_fotos.append(f"'../assets/productos/con_marco_blanco/191_1_Horizontal_1200x630/{f}'")
    
fondant_fotos_str = "[" + ", ".join(fondant_js_fotos) + "]"
fondant_main_foto = f"'../assets/productos/con_marco_blanco/191_1_Horizontal_1200x630/{fondant_fotos[0]}'" if fondant_fotos else "''"

new_category = f"""{{
        id: 'fondant-personalizadas', nombre: 'Galletas de Fondant Personalizadas', ico: '🍪',
        foto: {fondant_main_foto},
        fotos: {fondant_fotos_str},
        titulo: 'Galletas de Fondant Personalizadas',
        texto: `<p><strong>Diseños Únicos y Artesanales en Fondant</strong></p>
        <p>Las galletas decoradas con fondant son verdaderas obras de arte comestibles. Perfectas para cualquier temática, desde personajes infantiles (como Mario Bros) hasta diseños corporativos o detalles elegantes para bodas.</p>
        <p>Utilizamos fondant de la más alta calidad sobre nuestras tradicionales galletas de mantequilla, logrando un equilibrio perfecto entre un diseño espectacular y un sabor inigualable.</p>`
      }},"""

html = html.replace('const EVENTOS = [', 'const EVENTOS = [\n      ' + new_category)

# But wait, in renderEventos we do:
# const imgUrl = f.startsWith('http') ? f : (e.foto ? e.foto : REF_BASE + f);
# Actually in renderEventos: e.foto is used directly. For the gallery:
# const ejemplos = (e.fotos || []).map(f => REF_BASE + f);
# This will prepend REF_BASE to the fondant fotos, breaking them!
# So for fondant, we must trick it, or modify renderEventos to check for '../'
# Let's modify renderEventos just slightly.
render_eventos_old = "const ejemplos = (e.fotos || []).map(f => REF_BASE + f);"
render_eventos_new = "const ejemplos = (e.fotos || []).map(f => f.startsWith('../') ? f : REF_BASE + f);"
html = html.replace(render_eventos_old, render_eventos_new)

# 4. Remove CSS frame-overlay
css_overlay_regex = r'\.product-card > \.relative \.frame-overlay \{[^\}]+\}'
html = re.sub(css_overlay_regex, '', html)
html = html.replace('<div class="frame-overlay"></div>', '')

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated HTML successfully")
