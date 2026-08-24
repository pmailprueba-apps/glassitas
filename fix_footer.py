import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire footer
pattern = r'<footer class="w-full mt-asymmetric-offset.*?</footer>'
new_footer = """<footer class="w-full bg-surface-bright border-t border-terracotta/20 pt-20 pb-12 mt-20">
  <div class="max-w-container-max mx-auto px-margin-mobile md:px-gutter">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
      
      <!-- Col 1: Brand & Info -->
      <div class="md:col-span-2 flex flex-col items-center md:items-start text-center md:text-left">
        <a href="#" class="inline-block mb-6">
          <img src="../assets/logo/logo_transparente.png" alt="Glassitas" class="h-20 md:h-24 w-auto object-contain drop-shadow-md">
        </a>
        <p class="text-on-surface-variant leading-relaxed max-w-sm mb-6 text-lg">
          Fábrica especializada en galletas personalizadas. Artesanía en cada detalle para bodas, bautizos, empresas y celebraciones únicas.
        </p>
        <p class="text-on-surface-variant flex items-center justify-center md:justify-start gap-2 font-medium">
          <span class="material-symbols-outlined text-terracotta">location_on</span>
          San Luis Potosí, México
        </p>
      </div>

      <!-- Col 2: Enlaces -->
      <div class="text-center md:text-left">
        <h4 class="font-bold text-deep-teal mb-6 uppercase tracking-wider text-sm">Explorar</h4>
        <ul class="space-y-4">
          <li><a href="#catalogo-galletas" class="text-on-surface-variant hover:text-terracotta transition-colors duration-200">Catálogo y Galería</a></li>
          <li><a href="#mayoreo" class="text-on-surface-variant hover:text-terracotta transition-colors duration-200">Precios de Mayoreo</a></li>
          <li><a href="#proceso" class="text-on-surface-variant hover:text-terracotta transition-colors duration-200">Cómo trabajamos</a></li>
          <li><a href="../preguntas-frecuentes.html" class="text-on-surface-variant hover:text-terracotta transition-colors duration-200">Preguntas Frecuentes</a></li>
        </ul>
      </div>

      <!-- Col 3: Contacto -->
      <div class="text-center md:text-left">
        <h4 class="font-bold text-deep-teal mb-6 uppercase tracking-wider text-sm">Contacto</h4>
        <ul class="space-y-4">
          <li>
            <a href="https://wa.me/5214446506790" target="_blank" class="inline-flex items-center justify-center md:justify-start gap-2 text-on-surface-variant hover:text-[#25D366] transition-colors duration-200 font-medium">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.297-.497.1-.198.05-.371-.025-.52-.074-.149-.668-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
              WhatsApp (+52 444 650 6790)
            </a>
          </li>
          <li><a href="#" class="text-on-surface-variant hover:text-terracotta transition-colors duration-200">Políticas de Privacidad</a></li>
        </ul>
      </div>

    </div>

    <!-- Copyright -->
    <div class="pt-8 border-t border-gray-200/70 flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-gray-500 font-medium">
      <p>© 2026 Glassitas. Todos los derechos reservados.</p>
      <p>Hecho con pasión en San Luis Potosí</p>
    </div>
  </div>
</footer>"""

html = re.sub(pattern, new_footer, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Footer section redesigned!")
