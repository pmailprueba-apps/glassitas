import re

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update colors to pink pastel
html = html.replace('"background": "#fbf9f4"', '"background": "#F8DCD1"')
html = html.replace('"surface-bright": "#fbf9f4"', '"surface-bright": "#F8DCD1"')

# Also make the body background color use the tailwind class `bg-background`
html = html.replace('<body class="', '<body class="bg-background ')
if '<body class="' not in html:
    html = html.replace('<body>', '<body class="bg-background font-body-lg text-on-surface">')

# 2. Fix the Hero Image
hero_img_regex = r'<img alt="Hero Cookies"[^>]*>'
new_hero_img = '<img alt="Galletas Decoradas Glassitas" class="w-full h-full object-cover product-img" src="../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0047ac48-1662-4bcc-88b1-e547cdc92e8e.jpg"/>'
html = re.sub(hero_img_regex, new_hero_img, html)

# 3. Fix Buttons
btn_contacto = r'<button class="tactile-btn bg-deep-teal text-off-white px-6 py-2 rounded-sm font-label-caps uppercase hidden md:block">Contacto</button>'
link_contacto = '<a href="https://wa.me/524445101553" target="_blank" class="tactile-btn bg-deep-teal text-off-white px-6 py-2 rounded-sm font-label-caps uppercase hidden md:block" style="text-decoration:none; display:inline-flex; align-items:center;">Contacto</a>'
html = html.replace(btn_contacto, link_contacto)

btn_explorar = r'<button class="tactile-btn bg-deep-teal text-off-white px-8 py-4 rounded-sm font-label-caps uppercase">Explorar Catálogo</button>'
link_explorar = '<a href="#catalogo-galletas" class="tactile-btn bg-deep-teal text-off-white px-8 py-4 rounded-sm font-label-caps uppercase" style="text-decoration:none; display:inline-flex; align-items:center; margin-top:16px;">Explorar Catálogo</a>'
html = html.replace(btn_explorar, link_explorar)

# Add ID to catalog section
cat_section_regex = r'<!-- Galletas Diseño Personalizado -->\s*<section class="max-w-container-max mx-auto px-margin-mobile md:px-gutter py-24'
html = re.sub(cat_section_regex, r'<!-- Galletas Diseño Personalizado -->\n<section id="catalogo-galletas" class="max-w-container-max mx-auto px-margin-mobile md:px-gutter py-24', html)

# 4. Remove fake sections
fake_sections_regex = r'<!-- Galletas con Impresión -->.*?<!-- Footer -->'
html = re.sub(fake_sections_regex, '<!-- Footer -->', html, flags=re.DOTALL)

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML corrections applied successfully")
