import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the Emojis from EVENTOS array
html = re.sub(r"ico: '.*?',\n", '', html)
html = re.sub(r"ico: '.*?'.*?nombre:", 'nombre:', html)

# Apply Double-Bezel layout (outer shell + inner core) to product cards
# Let's fix renderEventos first
# 1. Update the outer card shell
html = html.replace('<div class="product-card bg-white group cursor-pointer ${isExpanded ? \'expanded\' : \'\'} rounded-2xl p-4 md:p-6 border border-gray-100 hover:border-terracotta/20 hover:shadow-xl transition-all duration-300" onclick="selectEvento(\'${e.id}\')">',
                    '<div class="product-card group cursor-pointer ${isExpanded ? \'expanded\' : \'\'} relative p-2 md:p-3 bg-white/5 ring-1 ring-black/5 rounded-[2.5rem] transition-all duration-700 ease-[cubic-bezier(0.32,0.72,0,1)] hover:scale-[0.98]" onclick="selectEvento(\'${e.id}\')"><div class="relative w-full h-full bg-white rounded-[calc(2.5rem-0.75rem)] p-4 md:p-6 shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)] flex flex-col justify-between">')
                    
# Close the inner core div
html = html.replace('${expandHtml}\n        </div>`;', '${expandHtml}\n        </div></div>`;')

# Strip Emojis from rendering in H3: 
html = html.replace('${e.ico} ${e.nombre}</h3>', '${e.nombre}</h3>')

# Apply same to Mayoreo Formas
html = html.replace("ico: '⭕', ", "")
html = html.replace("ico: '🟦', ", "")
html = html.replace("ico: '▬', ", "")
html = html.replace("ico: '❤️', ", "")
html = html.replace('${f.ico} ${f.nombre}', '${f.nombre}')
html = html.replace('${f.ico} </span>', '</span>')
# The shapes HTML string builder
html = html.replace('<button class="shape-btn ${activo} flex items-center justify-center gap-2 p-3 md:p-4 rounded-xl border border-gray-200 transition-all font-semibold"', 
                    '<button class="shape-btn ${activo} group flex items-center justify-center p-3 md:p-4 rounded-full border border-gray-200 transition-all duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] hover:scale-[0.98] font-bold text-sm tracking-wide"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Kowalski aesthetics applied!")
