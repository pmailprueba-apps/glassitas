import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="global-marquee"' not in html:
    # 1. We need to extract all images. We can inject a small inline JS script inside the marquee 
    # to render the images, OR just do it server-side (in python) by parsing the FOTOS array.
    
    # Let's extract FOTOS array from JS:
    fotos_match = re.search(r'const FOTOS = \[(.*?)\];', html, re.DOTALL)
    if fotos_match:
        fotos_str = fotos_match.group(1)
        # remove quotes and trim
        fotos = [f.strip().strip("'").strip('"') for f in fotos_str.split(',') if f.strip()]
        
        # Build marquee HTML
        marquee_html = """
<!-- Global Marquee -->
<section id="global-marquee" class="py-12 bg-white overflow-hidden relative border-y border-terracotta/10">
    <div class="absolute top-0 bottom-0 left-0 w-24 bg-gradient-to-r from-white to-transparent z-10 pointer-events-none"></div>
    <div class="absolute top-0 bottom-0 right-0 w-24 bg-gradient-to-l from-white to-transparent z-10 pointer-events-none"></div>
    
    <div class="animate-infinite-scroll flex w-max gap-6 hover:[animation-play-state:paused]">
"""
        # Duplicate for infinite scroll
        all_fotos = fotos + fotos + fotos
        for i, f in enumerate(all_fotos):
            code = f'GL-{str((i % len(fotos)) + 1).zfill(3)}'
            f_url = f"../assets/productos/con_marco_blanco/{f}"
            marquee_html += f"""
        <div class="cursor-pointer relative rounded-2xl overflow-hidden ambient-shadow flex-shrink-0" style="width: 280px; height: 280px;" onclick="openLightbox('{f_url}', 'Catálogo General', '{code}'); event.stopPropagation();">
            <img src="{f_url}" alt="Galleta" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" loading="lazy">
            <span class="absolute top-3 left-3 bg-deep-teal/90 text-white text-xs font-semibold px-2 py-1 rounded shadow-sm z-20">{code}</span>
        </div>"""
        
        marquee_html += """
    </div>
</section>
"""
        
        # Inject before catalogo-galletas
        html = html.replace('<!-- Galletas Diseño Personalizado -->', marquee_html + '\n<!-- Galletas Diseño Personalizado -->')
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Marquee added successfully!")
    else:
        print("Could not find FOTOS array!")
else:
    print("Marquee already exists!")
