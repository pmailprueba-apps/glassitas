import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix catalog h2
old_h2_cat = '<h2 class="text-2xl font-bold text-deep-teal mb-4">Galletas Diseño Personalizado</h2>'
new_h2_cat = '<h2 class="text-3xl md:text-5xl font-bold tracking-tight text-deep-teal mb-4 text-center">Galletas de Diseño Personalizado</h2>'
html = html.replace(old_h2_cat, new_h2_cat)

# Fix mayoreo h2 (remove font-serif, make it text-3xl md:text-5xl for consistency)
old_h2_mayoreo = '<h2 class="text-6xl font-bold font-serif text-deep-teal mb-2">Mayoreo — precios por volumen</h2>'
new_h2_mayoreo = '<h2 class="text-3xl md:text-5xl font-bold tracking-tight text-deep-teal mb-6">Mayoreo — Precios por Volumen</h2>'
html = html.replace(old_h2_mayoreo, new_h2_mayoreo)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("H2 tags fixed!")
