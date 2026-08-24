import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

css_addition = """
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-scroll {
            animation: scroll 30s linear infinite;
            display: inline-flex;
            width: max-content;
        }
        .animate-scroll:hover {
            animation-play-state: paused;
        }
"""
html = html.replace('</style>', css_addition + '</style>')

old_js = """          const ejemplos = (e.fotos || []);
          const galleryHtml = ejemplos.map((f, index) => {
            const code = 'GL-' + String(index + 1).padStart(3, '0');
            return `
            <div class="gallery-item cursor-pointer relative w-full rounded-lg overflow-hidden ambient-shadow" onclick=\"openLightbox('${f}', '${e.nombre}', '${code}'); event.stopPropagation();\">
              <img src="${f}" alt="${e.nombre}" class="w-full h-full object-cover" loading="lazy">
              
              <span class="id-badge absolute top-2 left-2 bg-deep-teal/90 text-white text-xs font-semibold px-2 py-1 rounded shadow-sm z-20">${code}</span>
            </div>
            `;
          }).join('');"""

new_js = """          const ejemplos = (e.fotos || []);
          const allItems = [...ejemplos, ...ejemplos];
          const galleryHtml = allItems.map((f, index) => {
            const originalIndex = index % ejemplos.length;
            const code = 'GL-' + String(originalIndex + 1).padStart(3, '0');
            return `
            <div class="cursor-pointer relative rounded-2xl overflow-hidden ambient-shadow flex-shrink-0" style="width: 250px; height: 250px;" onclick=\"openLightbox('${f}', '${e.nombre}', '${code}'); event.stopPropagation();\">
              <img src="${f}" alt="${e.nombre}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy">
              <span class="absolute top-2 left-2 bg-deep-teal/90 text-white text-xs font-semibold px-2 py-1 rounded shadow-sm z-20">${code}</span>
            </div>
            `;
          }).join('');"""

html = html.replace(old_js, new_js)

old_expand_body = """              <div class="expand-gallery">
                ${galleryHtml}
              </div>"""

new_expand_body = """              <div class="overflow-hidden relative w-full mt-6 -mx-2 px-2 py-2">
                <!-- Fade edges -->
                <div class="absolute top-0 bottom-0 left-0 w-8 bg-gradient-to-r from-white to-transparent z-10 pointer-events-none"></div>
                <div class="absolute top-0 bottom-0 right-0 w-8 bg-gradient-to-l from-white to-transparent z-10 pointer-events-none"></div>
                
                <div class="animate-scroll gap-4">
                  ${galleryHtml}
                </div>
              </div>"""

html = html.replace(old_expand_body, new_expand_body)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Carousel added successfully!")
