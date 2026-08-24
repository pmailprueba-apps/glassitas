import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update fonts link
old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600&amp;family=Libre+Caslon+Text:wght@400;700&amp;display=swap" rel="stylesheet"/>'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"/>'
html = html.replace(old_fonts, new_fonts)

# 2. Update Tailwind font configuration
html = html.replace('"Libre Caslon Text"', '"Playfair Display", "serif"')
html = html.replace('"Hanken Grotesk"', '"Montserrat", "sans-serif"')

# 3. Enhance the Logo styling in the Hero section
old_logo = '<img src="../assets/logo/logo_transparente.png" alt="Glassitas Logo" class="w-56 md:w-72 mb-8 drop-shadow-md">'
new_logo = '''<div class="relative inline-block mb-10">
    <div class="absolute inset-0 bg-white/60 blur-[60px] rounded-full scale-[2.0] z-0"></div>
    <img src="../assets/logo/logo_transparente.png" alt="Glassitas Logo" class="relative z-10 w-64 md:w-[28rem] drop-shadow-2xl transition-transform duration-700 hover:scale-105" style="filter: drop-shadow(0 15px 25px rgba(0,75,77,0.15));">
</div>'''
html = html.replace(old_logo, new_logo)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fonts and Logo updated!")
