import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the outer wrapper
old_outer = r'<div class="product-card group cursor-pointer \${isExpanded \? \'expanded\' : \'\'} relative p-2 md:p-3 bg-white/5 ring-1 ring-black/5 rounded-\[2\.5rem\] transition-all duration-700 ease-\[cubic-bezier\(0\.32,0\.72,0,1\)\] hover:scale-\[0\.98\]"'
new_outer = r'<div class="product-card group ${isExpanded ? \'expanded md:col-span-full cursor-default\' : \'cursor-pointer hover:scale-[0.98]\'} relative p-2 md:p-3 bg-white/5 ring-1 ring-black/5 rounded-[2.5rem] transition-all duration-700 ease-[cubic-bezier(0.32,0.72,0,1)]"'
html = re.sub(old_outer, new_outer, html)

# Fix the image container
old_img = r'<div class="relative w-full rounded-xl overflow-hidden ambient-shadow mb-6" style="aspect-ratio: 1/1;">'
new_img = r'<div class="relative w-full rounded-xl overflow-hidden ambient-shadow mb-6 ${isExpanded ? \'hidden\' : \'block\'}" style="aspect-ratio: 1/1;">'
html = html.replace(old_img, new_img)

# Fix the title
old_title = r'<h3 class="text-lg md:text-xl leading-tight font-serif font-bold text-deep-teal mb-3 group-hover:text-terracotta transition-colors active-scale">\${e\.nombre}</h3>'
new_title = r'<h3 class="text-lg md:text-xl leading-tight font-serif font-bold text-deep-teal mb-3 group-hover:text-terracotta transition-colors active-scale ${isExpanded ? \'hidden\' : \'block\'}">${e.nombre}</h3>'
html = html.replace(old_title, new_title)

# Fix the description paragraph
old_desc = r'<p class="text-base text-on-surface-variant">\${isExpanded \? \'Cerrar detalles\' : \'Ver descripción y ejemplos\'}</p>'
new_desc = r'<p class="text-base text-on-surface-variant ${isExpanded ? \'hidden\' : \'block\'}">Ver descripción y ejemplos</p>'
html = html.replace(old_desc, new_desc)

# Fix the scroll JS
old_scroll = r"const activeEl = document.querySelector('.event-card.expanded');"
new_scroll = r"const activeEl = document.querySelector('.product-card.expanded');"
html = html.replace(old_scroll, new_scroll)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Expanded logic fixed!")
