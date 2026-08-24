import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the second "fontFamily": {...} completely
html = re.sub(r'"fontFamily":\s*\{[^}]+\},', '', html, flags=re.DOTALL)

# Re-write the first one to be perfectly clean
old_config = """                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        serif: ['"Outfit"', 'sans-serif'],
                    },"""
new_config = """                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        serif: ['"Outfit"', 'sans-serif'],
                        "display-lg-mobile": ['"Outfit"', "sans-serif"],
                        "body-lg": ['"Plus Jakarta Sans"', "sans-serif"],
                        "product-code": ['"Plus Jakarta Sans"', "sans-serif"],
                        "display-lg": ['"Outfit"', "sans-serif"],
                        "body-md": ['"Plus Jakarta Sans"', "sans-serif"],
                        "label-caps": ['"Plus Jakarta Sans"', "sans-serif"],
                        "headline-md": ['"Outfit"', "sans-serif"]
                    },"""
html = html.replace(old_config, new_config)

# Fix the H3 font size so it doesn't wrap awkwardly. 
html = html.replace('text-xl font-serif font-bold text-deep-teal mb-2', 'text-lg md:text-xl leading-tight font-serif font-bold text-deep-teal mb-3')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Config fixed!")
