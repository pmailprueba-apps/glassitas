import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# First, revert the messy half-fixes to have a clean state for regex
html = html.replace('assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0', 'assets/productos/con_marco_blanco/0')

# Now apply the correct directory to ALL of them in the marquee section only!
# The marquee section is between <section id="global-marquee"> and </section>
def fix_marquee_images(match):
    marquee_html = match.group(0)
    # Inside marquee, replace all base image paths with the subfolder
    marquee_html = marquee_html.replace('assets/productos/con_marco_blanco/', 'assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/')
    return marquee_html

html = re.sub(r'<section id="global-marquee".*?</section>', fix_marquee_images, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("All marquee images fixed!")
