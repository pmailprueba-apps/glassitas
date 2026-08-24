import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Apply Double-Bezel layout to MAYOREO cards as well
# Current Mayoreo HTML:
# <div class="product-card">
#   <div class="thumb"><img src="${prod.img}" alt="Galletas ${formaInfo.verbo} ${prod.talla}" loading="lazy"></div>

html = html.replace('<div class="product-card">',
                    '<div class="product-card group relative p-2 md:p-3 bg-white/5 ring-1 ring-black/5 rounded-[2.5rem] transition-all duration-700 ease-[cubic-bezier(0.32,0.72,0,1)] hover:scale-[0.98]"><div class="relative w-full h-full bg-white rounded-[calc(2.5rem-0.75rem)] p-4 shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)] flex flex-col justify-between">')

# Close Mayoreo Double Bezel
html = html.replace('Cotizar por WhatsApp\n              </a>\n            </div>\n          </div>`;',
                    'Cotizar por WhatsApp\n              </a>\n            </div>\n          </div></div>`;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Mayoreo Kowalski applied!")
