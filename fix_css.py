import re

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update REF_BASE back to original
html = html.replace("const REF_BASE = 'contenido/referencia_fotogalletas/categorias_con_marco/';", "const REF_BASE = 'contenido/referencia_fotogalletas/categorias/';")

# In renderEventos we had: const ejemplos = (e.fotos || []).map(f => f.startsWith('../') ? f : REF_BASE + f);
# Wait, let's keep that because the fondant photos still need the full path to con_marco_blanco!
# The fondant photos are using '../assets/productos/con_marco_blanco/...' and we SHOULD NOT apply the frame-overlay to them!
# Wait! If we apply .frame-overlay via CSS to ALL galleries, the fondant photos (which already have frames) will get a SECOND frame overlaid on them!
# We need to distinguish between fondant photos (which already have frames) and other photos (which need CSS frames).
# Let's add a property to the category: `has_frame: true` for fondant.
fondant_str = "id: 'fondant-personalizadas', nombre: 'Galletas de Fondant Personalizadas', ico: '🍪',"
html = html.replace(fondant_str, fondant_str + " has_frame: true,")

# Now in renderEventos, conditionally add .frame-overlay
# old gallery item:
gallery_regex = r'<div class="gallery-item cursor-pointer" onclick="cotizarEjemplo\(\'\$\{e\.nombre\}\'\); event\.stopPropagation\(\);">\s*<img src="\$\{f\}" alt="\$\{e\.nombre\}" loading="lazy">\s*<span class="id-badge">\$\{code\}</span>\s*</div>'
new_gallery = """<div class="gallery-item cursor-pointer relative w-full rounded-lg overflow-hidden ambient-shadow" onclick="cotizarEjemplo('${e.nombre}'); event.stopPropagation();">
              <img src="${f}" alt="${e.nombre}" class="w-full h-full object-cover" loading="lazy">
              ${e.has_frame ? '' : '<div class="frame-overlay-vertical absolute inset-0 pointer-events-none z-10" style="background-image: url(\\'../assets/logo/escaletas/escaleta%20insta.png\\'); background-size: 100% 100%; background-position: center; background-repeat: no-repeat;"></div>'}
              <span class="id-badge absolute top-2 left-2 bg-deep-teal/90 text-white text-xs font-semibold px-2 py-1 rounded shadow-sm z-20">${code}</span>
            </div>"""
html = re.sub(gallery_regex, new_gallery, html)

# For the main event card (thumb):
# Find where the thumb is generated:
# <div class="relative w-full rounded-sm overflow-hidden ambient-shadow mb-6">
#   <div class="inner-border"></div>
#   <div class="absolute top-4 right-4 z-20 bg-off-white px-3 py-1 rounded-full border border-terracotta font-product-code text-terracotta">${e.ico}</div>
#   <img alt="${e.nombre}" class="w-full h-full object-cover product-img" loading="lazy" src="${imgUrl}">
# </div>
thumb_regex = r'<div class="relative w-full rounded-sm overflow-hidden ambient-shadow mb-6">\s*<div class="inner-border"></div>\s*<div class="absolute top-4 right-4[^>]+>\$\{e\.ico\}</div>\s*<img [^>]+>\s*</div>'
new_thumb = """<div class="relative w-full rounded-sm overflow-hidden ambient-shadow mb-6 thumb-container">
            <div class="inner-border pointer-events-none z-20"></div>
            <div class="absolute top-4 right-4 z-20 bg-off-white px-3 py-1 rounded-full border border-terracotta font-product-code text-terracotta">${e.ico}</div>
            <img alt="${e.nombre}" class="w-full h-full object-cover product-img" loading="lazy" src="${imgUrl}">
            ${e.has_frame ? '' : '<div class="frame-overlay-horizontal absolute inset-0 pointer-events-none z-10" style="background-image: url(\\'../assets/logo/escaletas/escaleta%20horizontal%202.png\\'); background-size: 100% 100%; background-position: center; background-repeat: no-repeat;"></div>'}
          </div>"""
html = re.sub(thumb_regex, new_thumb, html)

# Update CSS for aspect ratios
css_aspect_old = r'\.product-card > \.relative \{ aspect-ratio: 1/1; \}\s*\.product-card\.expanded > \.relative \{ aspect-ratio: 21/9; max-height: 400px; \}'
css_aspect_new = """
  /* Main cards use horizontal frame proportion */
  .product-card > .relative.thumb-container { aspect-ratio: 2816 / 1536; }
  .product-card.expanded > .relative.thumb-container { aspect-ratio: 2816 / 1536; max-height: 350px; }
  
  /* Gallery items use vertical/insta frame proportion */
  .gallery-item { aspect-ratio: 1856 / 2304; }
"""
html = re.sub(css_aspect_old, css_aspect_new, html)

# Update expand-gallery grid to be smaller
gallery_grid_old = r'\.expand-gallery \{\s*display: grid;\s*grid-template-columns: repeat\(auto-fill, minmax\(140px, 1fr\)\);\s*gap: 16px;\s*margin-top: 24px;\s*margin-bottom: 24px;\s*\}'
gallery_grid_new = """.expand-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    gap: 12px;
    margin-top: 24px;
    margin-bottom: 24px;
  }
  @media (min-width: 768px) {
    .expand-gallery {
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
      gap: 16px;
    }
  }"""
html = re.sub(gallery_grid_old, gallery_grid_new, html)

# Also remove .gallery-item img aspect-ratio to let the container drive it
gallery_item_img_regex = r'\.gallery-item img \{\s*width: 100%;\s*aspect-ratio: 1/1;\s*object-fit: cover;\s*\}'
html = re.sub(gallery_item_img_regex, '', html)

# 4. Change Hero Image
hero_regex = r'<img alt="Galletas Decoradas Glassitas"[^>]*src="\.\./assets/productos/con_marco_blanco/[^"]+"'
hero_new = '<img alt="Galletas Decoradas Glassitas" class="w-full h-full object-cover product-img" src="../assets/productos/web/02ccee75-86e6-4cc2-8073-1cf83f97864f.jpg"'
html = re.sub(hero_regex, hero_new, html)

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("CSS adjustments applied.")
