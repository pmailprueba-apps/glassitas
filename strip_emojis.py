import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Strip any residual emoji icons from EVENTOS object directly in the data structure
html = re.sub(r"ico: '.*?',\s*", "", html)
# If some were left behind as just empty strings or something
html = re.sub(r"ico: '',\s*", "", html)

# From the product cards
html = html.replace('${e.ico} ', '')

# Fix font wrapping on Mayoreo section while we're here
html = html.replace('<div class="name">${formaInfo.nombre} · ${prod.talla}</div>', '<div class="text-lg md:text-xl font-serif font-bold text-deep-teal mb-1 leading-tight">${formaInfo.nombre} <br class="hidden md:block"> <span class="text-terracotta text-sm md:text-base">${prod.talla}</span></div>')
html = html.replace('<div class="spec">${formaInfo.verbo} personalizadas</div>', '<div class="text-sm font-medium text-on-surface-variant mb-4">${formaInfo.verbo} personalizadas</div>')


# Ensure all shapes buttons lose their emojis
# They are in this array:
#     const FORMAS = [
#      { id: 'circular',    nombre: 'Circulares',    verbo: 'circulares' },
html = html.replace("ico: '⭕', ", "")
html = html.replace("ico: '🟦', ", "")
html = html.replace("ico: '▬', ", "")
html = html.replace("ico: '❤️', ", "")


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Emojis stripped and text refined!")
