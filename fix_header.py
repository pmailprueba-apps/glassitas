import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix phone number globally in this file
html = html.replace('5214446506790', '524445101553')
html = html.replace('+52 444 650 6790', '+52 444 510 1553')

# Fix header design
old_header = """<header class="w-full top-0 sticky bg-background dark:bg-background z-50">
<div class="flex justify-between items-center max-w-container-max mx-auto px-margin-mobile md:px-gutter py-unit">
<div class="flex items-center gap-2">
<img src="../assets/logo/logo_transparente.png" alt="Glassitas Logo" class="h-16 w-auto object-contain hover:scale-105 transition-transform">
</div>
<nav class="hidden md:flex gap-8">
<a class="text-terracotta font-bold border-b-2 border-terracotta pb-1" href="#">Galería</a>
<a class="text-on-surface-variant font-medium hover:text-terracotta transition-colors active-scale" href="#mayoreo">Mayoreo</a>
<a class="text-on-surface-variant font-medium hover:text-terracotta transition-colors active-scale" href="../preguntas-frecuentes.html">Preguntas</a>
</nav>
<a href="https://wa.me/524445101553" target="_blank" class="tactile-btn bg-deep-teal text-off-white px-6 py-2 rounded-sm text-sm font-bold uppercase tracking-wider uppercase hidden md:block" style="text-decoration:none; display:inline-flex; align-items:center;">Contacto</a>
<button class="md:hidden text-primary">
<span class="material-symbols-outlined">menu</span>
</button>
</div>
</header>"""

new_header = """<header class="w-full top-0 sticky bg-surface-bright/90 backdrop-blur-md z-50 border-b border-terracotta/10 shadow-sm transition-all duration-300">
<div class="flex justify-between items-center max-w-container-max mx-auto px-6 md:px-12 py-3">
<div class="flex items-center gap-2">
<a href="#" class="inline-block relative group">
  <div class="absolute inset-0 bg-white/40 blur-xl rounded-full scale-150 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
  <img src="../assets/logo/logo_transparente.png" alt="Glassitas Logo" class="h-14 md:h-20 w-auto object-contain relative z-10 transition-transform duration-500 group-hover:scale-105">
</a>
</div>
<nav class="hidden md:flex items-center gap-10 bg-white/60 px-8 py-3 rounded-full border border-terracotta/10 shadow-[inset_0_1px_1px_rgba(255,255,255,1)]">
<a class="text-deep-teal font-bold border-b-2 border-terracotta pb-0.5 hover:text-terracotta transition-colors" href="#">Galería</a>
<a class="text-on-surface-variant font-semibold hover:text-terracotta transition-colors active-scale" href="#mayoreo">Mayoreo</a>
<a class="text-on-surface-variant font-semibold hover:text-terracotta transition-colors active-scale" href="../preguntas-frecuentes.html">Preguntas Frecuentes</a>
</nav>
<a href="https://wa.me/524445101553" target="_blank" class="tactile-btn bg-deep-teal text-white px-7 py-3 rounded-full text-sm font-bold uppercase tracking-widest hidden md:flex items-center gap-2 shadow-lg hover:shadow-xl hover:bg-[#00383a]">
<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.297-.497.1-.198.05-.371-.025-.52-.074-.149-.668-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
Contacto
</a>
<button class="md:hidden text-deep-teal hover:text-terracotta active-scale">
<span class="material-symbols-outlined text-3xl">menu</span>
</button>
</div>
</header>"""

if old_header in html:
    html = html.replace(old_header, new_header)
else:
    print("WARNING: Header exact match not found. Attempting regex...")
    pattern = r'<header class="w-full top-0 sticky.*?</header>'
    html = re.sub(pattern, new_header, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Phone numbers and Header redesigned!")
