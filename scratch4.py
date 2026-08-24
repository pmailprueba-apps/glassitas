import re

with open('tienda.html', 'r', encoding='utf-8') as f:
    tienda = f.read()

# Extract Mayoreo and Proceso
mayoreo_match = re.search(r'<!-- Mayoreo -->.*?<!-- CTA -->', tienda, re.DOTALL)
if mayoreo_match:
    mayoreo_html = mayoreo_match.group(0)
    # Convert old styles to tailwind where possible, or just keep it as is, but it uses CSS variables from tienda.
    # The old CSS uses var(--accent), var(--border), var(--surface) etc.
    # So I will inject the necessary CSS variables for these specific sections to work without rebuilding them from scratch,
    # or just convert them directly to Tailwind inline classes.
    # Converting to Tailwind is better for consistency.
    
    tailwind_mayoreo = """
<!-- Mayoreo -->
<section id="mayoreo" class="py-24 border-y border-terracotta/20 bg-surface-bright">
    <div class="max-w-container-max mx-auto px-margin-mobile md:px-gutter">
      <h2 class="font-display-lg text-deep-teal mb-2">Mayoreo — precios por volumen</h2>
      <p class="font-body-lg text-on-surface-variant mb-12">Precios especiales para pedidos desde 100 galletas (ideal para empresas y eventos grandes)</p>
      
      <div class="overflow-x-auto w-full mb-8">
        <table class="w-full text-left bg-white rounded-lg shadow-sm overflow-hidden min-w-[600px]">
          <thead class="bg-deep-teal text-white">
            <tr>
              <th class="p-4 font-semibold">Forma</th>
              <th class="p-4 font-semibold">Tamaño</th>
              <th class="p-4 font-semibold">100+ unidades</th>
              <th class="p-4 font-semibold">500+ unidades</th>
              <th class="p-4 font-semibold">1000+ unidades</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">4.0 cm</td><td class="p-4">$18</td><td class="p-4">$17</td><td class="p-4">$16</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">5.0 cm</td><td class="p-4">$23</td><td class="p-4">$22</td><td class="p-4">$21</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">7.5 cm</td><td class="p-4">$38</td><td class="p-4">$37</td><td class="p-4">$36</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">8.5 cm</td><td class="p-4">$43</td><td class="p-4">$42</td><td class="p-4">$41</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Rectangular</td><td class="p-4 font-medium text-deep-teal">6.0 × 4.5 cm</td><td class="p-4">$24</td><td class="p-4">$23</td><td class="p-4">$22</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Rectangular</td><td class="p-4 font-medium text-deep-teal">7.5 × 5.5 cm</td><td class="p-4">$34</td><td class="p-4">$33</td><td class="p-4">$32</td></tr>
          </tbody>
        </table>
      </div>
      <p class="text-sm text-on-surface-variant">* Precios por galleta envasada individualmente, referenciales. Los precios finales dependen del diseño, cantidad y tiempos — escríbenos para tu cotización sin compromiso.</p>
    </div>
</section>

<!-- Proceso -->
<section id="proceso" class="py-24 bg-background">
    <div class="max-w-container-max mx-auto px-margin-mobile md:px-gutter">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        
        <div class="bg-white p-8 rounded-lg border border-terracotta/10 ambient-shadow">
          <span class="block font-display-lg text-4xl text-terracotta opacity-60 mb-4">01</span>
          <h4 class="font-body-lg font-semibold text-deep-teal mb-2">Elige y cotiza</h4>
          <p class="text-on-surface-variant">Selecciona el evento, la forma y la cantidad, o escríbenos con tu idea por WhatsApp.</p>
        </div>
        
        <div class="bg-white p-8 rounded-lg border border-terracotta/10 ambient-shadow">
          <span class="block font-display-lg text-4xl text-terracotta opacity-60 mb-4">02</span>
          <h4 class="font-body-lg font-semibold text-deep-teal mb-2">Envías tu diseño</h4>
          <p class="text-on-surface-variant">Comparte tu logo, foto o referencia. Aprobamos juntos el diseño definitivo.</p>
        </div>
        
        <div class="bg-white p-8 rounded-lg border border-terracotta/10 ambient-shadow">
          <span class="block font-display-lg text-4xl text-terracotta opacity-60 mb-4">03</span>
          <h4 class="font-body-lg font-semibold text-deep-teal mb-2">Producimos</h4>
          <p class="text-on-surface-variant">Galletas gourmet de mantequilla con fondant e impresión en papel de azúcar.</p>
        </div>
        
        <div class="bg-white p-8 rounded-lg border border-terracotta/10 ambient-shadow">
          <span class="block font-display-lg text-4xl text-terracotta opacity-60 mb-4">04</span>
          <h4 class="font-body-lg font-semibold text-deep-teal mb-2">Recibes</h4>
          <p class="text-on-surface-variant">Envasadas individualmente para mantener el sabor hasta 6 meses. Entrega en SLP.</p>
        </div>
        
      </div>
    </div>
</section>
"""

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# 1. Update Navigation Links
nav_mayoreo = r'<a class="text-on-surface-variant font-medium hover:text-terracotta transition-colors duration-300" href="#">Mayoreo</a>'
nav_preguntas = r'<a class="text-on-surface-variant font-medium hover:text-terracotta transition-colors duration-300" href="#">Preguntas</a>'
index = index.replace(nav_mayoreo, '<a class="text-on-surface-variant font-medium hover:text-terracotta transition-colors duration-300" href="#mayoreo">Mayoreo</a>')
index = index.replace(nav_preguntas, '<a class="text-on-surface-variant font-medium hover:text-terracotta transition-colors duration-300" href="../preguntas-frecuentes.html">Preguntas</a>')

# 2. Append Sections before footer
index = index.replace('<!-- Footer -->', tailwind_mayoreo + '\n<!-- Footer -->')

# 3. Add CSS for grid spanning and fixed height
css_add = """
  .product-card.expanded { grid-column: 1 / -1; }
  .product-card.expanded > .relative { max-height: 400px; aspect-ratio: auto !important; }
  .product-card.expanded > .relative img { object-position: center; }
"""
index = index.replace('</style>', css_add + '\n</style>')

# Ensure "aspect-square" is on the relative container, and when expanded we override it.
# Actually, tailwind "aspect-square" class forces the aspect ratio, which will override the normal CSS if it has higher specificity.
# Let's remove "aspect-square" from the HTML and add it to standard CSS so we can easily override it.
index = index.replace('aspect-square', '')
css_aspect = """
  .product-card > .relative { aspect-ratio: 1/1; }
  .product-card.expanded > .relative { aspect-ratio: 21/9; max-height: 400px; }
"""
index = index.replace('</style>', css_aspect + '\n</style>')


with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

print("Applied fixes successfully")
