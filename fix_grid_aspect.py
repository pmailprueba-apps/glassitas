import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the grid image from object-cover to object-contain bg-white
# In renderEventos:
# <div class="relative thumb-container rounded-t-lg overflow-hidden ambient-shadow w-full" style="aspect-ratio: 1/1;">
# <img alt="${e.nombre}" class="w-full h-full object-cover" src="${e.foto}" loading="lazy"/>
old_img = 'class="w-full h-full object-cover" src="${e.foto}"'
new_img = 'class="w-full h-full object-contain bg-white" src="${e.foto}"'
html = html.replace(old_img, new_img)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Grid images set to object-contain bg-white!")
