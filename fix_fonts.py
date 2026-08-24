import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Google Fonts link
old_fonts = 'family=Montserrat:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap'
new_fonts = 'family=Plus+Jakarta+Sans:wght@400;500;600&family=Outfit:wght@300;400;600;700&display=swap'
html = html.replace(old_fonts, new_fonts)

# 2. Update CSS font-family
old_css_body = "font-family: 'Montserrat', sans-serif;"
new_css_body = "font-family: 'Plus Jakarta Sans', sans-serif;"
html = html.replace(old_css_body, new_css_body)

old_css_heading = "font-family: 'Playfair Display', serif;"
new_css_heading = "font-family: 'Outfit', sans-serif;"
html = html.replace(old_css_heading, new_css_heading)

# 3. Fix sizes for Hero headline
# Currently: text-display-lg text-primary font-bold tracking-tight mb-4
# Skill says: text-4xl md:text-6xl lg:text-7xl tracking-tighter leading-none
html = html.replace('text-display-lg text-primary font-bold tracking-tight mb-4', 'text-4xl md:text-6xl lg:text-7xl text-primary font-bold tracking-tighter leading-[1.1] mb-6')

# Hero subtitle
# Currently: text-headline-sm text-on-surface-variant mb-8
# Skill says: text-base text-gray-600 leading-relaxed max-w-[65ch]
html = html.replace('text-headline-sm text-on-surface-variant mb-8', 'text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[65ch] mb-8')

# Section titles
# Currently: text-display-md text-primary font-bold mb-8
# Skill says: text-3xl md:text-5xl tracking-tight mb-12
html = html.replace('text-display-md text-primary font-bold mb-8 text-center', 'text-3xl md:text-5xl text-primary font-bold tracking-tight mb-12 text-center')

# Other h2/h3 titles
html = html.replace('text-headline-md', 'text-2xl font-bold tracking-tight')
html = html.replace('text-title-lg', 'text-xl font-bold tracking-tight')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fonts and sizes updated based on design skills!")
