import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the logo before the h1
logo_html = '<img src="../assets/logo/logo_transparente.png" alt="Glassitas Logo" class="w-56 md:w-72 mb-8 drop-shadow-md">\n<h1 class="font-display-lg-mobile md:font-display-lg text-deep-teal mb-6">Galletas Gourmet Personalizadas</h1>'
html = html.replace('<h1 class="font-display-lg-mobile md:font-display-lg text-deep-teal mb-6">Galletas Gourmet Personalizadas</h1>', logo_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Logo added to Hero section!")
