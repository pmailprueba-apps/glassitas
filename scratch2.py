import re

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for frame-overlay and id-badge
css_styles = """
<style>
  .frame-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url('../assets/logo/escaletas/escaleta%20horizontal%202.png');
    background-size: 100% 100%;
    background-position: center;
    background-repeat: no-repeat;
    pointer-events: none;
    z-index: 10;
  }
  .gallery-item { position: relative; }
  .gallery-item .frame-overlay {
    background-image: url('../assets/logo/escaletas/escaleta%20insta.png');
    background-size: 100% 100%;
  }
  .gallery-item .id-badge {
    position: absolute;
    top: 8px;
    left: 8px;
    background: rgba(30, 99, 103, 0.9);
    color: #fff;
    font-size: 0.65rem;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 6px;
    letter-spacing: 0.5px;
    white-space: nowrap;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    backdrop-filter: blur(2px);
    pointer-events: none;
    z-index: 15;
  }
  
  /* Accordion styles */
  .expand-body {
    grid-column: 1 / -1;
    background: #F9F7F2;
    border: 1px solid rgba(196, 98, 49, 0.2);
    border-radius: 8px;
    padding: 24px;
    margin-top: 16px;
    display: none;
  }
  .product-card.expanded .expand-body {
    display: block;
  }
  .expand-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 16px;
    margin-top: 24px;
    margin-bottom: 24px;
  }
  .gallery-item img {
    width: 100%;
    aspect-ratio: 1/1;
    object-fit: cover;
    border-radius: 4px;
  }
  .wa-cat {
    display: inline-block;
    background-color: #004B4D;
    color: #F9F7F2;
    padding: 12px 24px;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
  }
</style>
"""

html = html.replace('</head>', css_styles + '</head>')

# Replace the static card HTML in the layout with an empty container for JS
static_cards_regex = r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">.*?<!-- Galletas con Impresión -->'
replacement = r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12" id="eventGrid"></div>\n</section>\n\n<!-- Galletas con Impresión -->'
html = re.sub(static_cards_regex, replacement, html, flags=re.DOTALL)

# Update the renderEventos function in the script
old_render_eventos = r'function renderEventos\(\) \{.*?\n    \}'
new_render_eventos = """function renderEventos() {
      const grid = document.getElementById('eventGrid');
      if (!grid) return;
      grid.innerHTML = EVENTOS.map(e => {
        const isExpanded = (e.id === eventoActivo);
        let expandHtml = '';
        if (isExpanded) {
          const waMsg = encodeURIComponent(`Hola Glassitas! Quiero cotizar galletas de ${e.nombre}. ¿Me pueden dar precios y tiempos?`);
          const ejemplos = (e.fotos || []).map(f => '../' + REF_BASE + f);
          const galleryHtml = ejemplos.map((f, index) => {
            const code = 'GL-' + String(index + 1).padStart(3, '0');
            return `
            <div class="gallery-item cursor-pointer" onclick="cotizarEjemplo('${e.nombre}'); event.stopPropagation();">
              <img src="${f}" alt="${e.nombre}" loading="lazy">
              <div class="frame-overlay"></div>
              <span class="id-badge">${code}</span>
            </div>
            `;
          }).join('');
          
          expandHtml = `
            <div class="expand-body" onclick="event.stopPropagation()">
              <div class="flex justify-between items-start mb-4">
                <h3 class="font-headline-md text-deep-teal">${e.titulo}</h3>
                <button class="text-terracotta hover:text-deep-teal transition-colors" onclick="selectEvento('${e.id}'); event.stopPropagation();">
                  <span class="material-symbols-outlined text-3xl">close</span>
                </button>
              </div>
              <div class="font-body-md text-on-surface-variant space-y-4">
                ${e.texto}
              </div>
              <div class="expand-gallery">
                ${galleryHtml}
              </div>
              <a class="wa-cat" href="https://wa.me/${WA}?text=${waMsg}" target="_blank">Cotizar ${e.nombre} por WhatsApp</a>
            </div>
          `;
        }
        
        return `
        <div class="product-card group cursor-pointer ${isExpanded ? 'expanded' : ''}" onclick="selectEvento('${e.id}')">
          <div class="relative w-full aspect-square rounded-sm overflow-hidden ambient-shadow mb-6">
            <div class="inner-border"></div>
            <img alt="${e.nombre}" class="w-full h-full object-cover product-img transition-transform duration-500 group-hover:scale-105" src="../${e.foto}" loading="lazy"/>
            <div class="frame-overlay"></div>
          </div>
          <h3 class="font-body-lg font-medium text-deep-teal mb-2 group-hover:text-terracotta transition-colors">${e.ico} ${e.nombre}</h3>
          <p class="font-body-md text-on-surface-variant">${isExpanded ? 'Cerrar detalles' : 'Ver descripción y ejemplos'}</p>
          ${expandHtml}
        </div>`;
      }).join('');
    }"""
    
html = re.sub(old_render_eventos, new_render_eventos, html, flags=re.DOTALL)

# Inject call to renderEventos() when DOM loads
html = html.replace('</script>', '  document.addEventListener("DOMContentLoaded", () => { renderEventos(); });\n</script>')

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML and JS updated successfully")
