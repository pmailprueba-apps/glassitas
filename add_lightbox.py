import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the onclick handler in renderEventos
old_onclick = r"onclick=\"cotizarEjemplo\('\$\{e\.nombre\}'\); event\.stopPropagation\(\);\""
new_onclick = r"onclick=\"openLightbox('${f}', '${e.nombre}', '${code}'); event.stopPropagation();\""
html = re.sub(old_onclick, new_onclick, html)

# 2. Add the Lightbox HTML before </body>
lightbox_html = """
<!-- Lightbox Modal -->
<div id="lightbox" class="fixed inset-0 z-[100] bg-black/90 hidden flex-col justify-center items-center p-4 md:p-8 backdrop-blur-sm transition-opacity duration-300 opacity-0" onclick="closeLightbox()">
  <button class="absolute top-4 right-4 md:top-8 md:right-8 text-white hover:text-terracotta transition-colors" onclick="closeLightbox(); event.stopPropagation();">
    <span class="material-symbols-outlined text-4xl">close</span>
  </button>
  <img id="lightbox-img" src="" class="max-w-full max-h-[75vh] object-contain rounded-lg shadow-2xl mb-6 border-4 border-white" onclick="event.stopPropagation();">
  <div class="text-center" onclick="event.stopPropagation();">
    <h3 id="lightbox-title" class="text-white font-headline-md mb-4"></h3>
    <a id="lightbox-wa" href="#" target="_blank" class="inline-flex items-center justify-center bg-[#25D366] text-white font-bold py-3 px-8 rounded-full shadow-lg hover:bg-deep-teal transition-all text-lg">
      <img src="../assets/logo/WhatsApp.svg.webp" class="w-6 h-6 mr-3">
      Cotizar este diseño
    </a>
  </div>
</div>

<script>
function openLightbox(imgSrc, nombreEvento, code) {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxWa = document.getElementById('lightbox-wa');
  const lightboxTitle = document.getElementById('lightbox-title');
  
  lightboxImg.src = imgSrc;
  lightboxTitle.textContent = `${nombreEvento} (${code})`;
  const msg = encodeURIComponent(`Hola Glassitas! Vi el diseño ${code} de ${nombreEvento} en su galería y me gustaría cotizar algo similar.`);
  lightboxWa.href = `https://wa.me/5214446506790?text=${msg}`;
  
  lightbox.classList.remove('hidden');
  lightbox.classList.add('flex');
  setTimeout(() => {
    lightbox.classList.remove('opacity-0');
  }, 10);
  
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  const lightbox = document.getElementById('lightbox');
  lightbox.classList.add('opacity-0');
  setTimeout(() => {
    lightbox.classList.add('hidden');
    lightbox.classList.remove('flex');
    document.body.style.overflow = '';
  }, 300);
}
</script>
</body>
"""
html = html.replace('</body>', lightbox_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Lightbox added!")
