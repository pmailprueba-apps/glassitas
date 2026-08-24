import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add .btn-premium to CSS
css_addition = """
        .btn-premium {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background-color: #004B4D;
            color: #ffffff;
            padding: 1rem 2rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform;
            text-decoration: none;
        }
        .btn-premium:hover {
            background-color: #00383a;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            transform: translateY(-2px);
        }
        .btn-premium:active {
            transform: scale(0.97) translateY(0);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
"""
html = html.replace('</style>', css_addition + '</style>')

# Replace wa-cat old CSS
old_wa_cat_css = """  .wa-cat {
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
    transition: background-color 0.3s, transform 0.2s;
    margin-top: 10px;
  }
  .wa-cat:hover {
    background-color: #C46231;
    transform: translateY(-2px);
  }"""
html = html.replace(old_wa_cat_css, "")

# Replace wa-btn old CSS
old_wa_btn_css = """  .wa-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background-color: #25D366; /* Verde WhatsApp */
    color: white;
    padding: 12px;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
    font-size: 0.95rem;
    transition: background-color 0.2s, transform 0.2s;
    margin-top: auto;
  }
  .wa-btn:hover {
    background-color: #1EBE5A;
    transform: translateY(-2px);
  }"""
html = html.replace(old_wa_btn_css, "")

# 2. Standardize all primary CTA classes in HTML to btn-premium
# Hero button:
old_hero_btn = '<a href="#catalogo-galletas" class="tactile-btn bg-deep-teal text-off-white px-8 py-4 rounded-sm text-sm font-bold uppercase tracking-wider uppercase" style="text-decoration:none; display:inline-flex; align-items:center; margin-top:16px;">Explorar Catálogo</a>'
new_hero_btn = '<a href="#catalogo-galletas" class="btn-premium mt-6">Explorar Catálogo</a>'
html = html.replace(old_hero_btn, new_hero_btn)

# WhatsApp button inside events card:
old_wa_cat_html = '<a class="wa-cat" href="https://wa.me/${WA}?text=${waMsg}" target="_blank">Cotizar ${e.nombre} por WhatsApp</a>'
new_wa_cat_html = '<a class="btn-premium mt-4 w-full text-center" href="https://wa.me/${WA}?text=${waMsg}" target="_blank">Cotizar ${e.nombre} por WhatsApp</a>'
html = html.replace(old_wa_cat_html, new_wa_cat_html)

# WhatsApp button inside product table:
old_wa_btn_html = '<a class="wa-btn"'
new_wa_btn_html = '<a class="btn-premium !bg-[#25D366] hover:!bg-[#1EBE5A] w-full text-center mt-auto"'
html = html.replace(old_wa_btn_html, new_wa_btn_html)

# 3. Standardize Radiuses and Shadows
# Event Cards (Gallery)
html = html.replace('class="product-card group cursor-pointer ${isExpanded ? \'expanded\' : \'\'}"', 'class="product-card bg-white group cursor-pointer ${isExpanded ? \'expanded\' : \'\'} rounded-2xl p-4 md:p-6 border border-gray-100 hover:border-terracotta/20 hover:shadow-xl transition-all duration-300"')
html = html.replace('class="relative w-full rounded-sm overflow-hidden ambient-shadow mb-6"', 'class="relative w-full rounded-xl overflow-hidden ambient-shadow mb-6"')

# Lightbox image
html = html.replace('id="lightbox-img" src="" class="max-w-full max-h-[75vh] object-contain rounded-lg shadow-2xl mb-6 border-4 border-white"', 'id="lightbox-img" src="" class="max-w-full max-h-[75vh] object-contain rounded-2xl shadow-2xl mb-6 border-4 border-white"')

# Mayoreo Cards
html = html.replace('rounded-lg ambient-shadow border border-gray-100', 'rounded-2xl ambient-shadow border border-gray-100')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Sweep completed!")
