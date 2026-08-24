import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix CSS for buttons (Kowalski Principles)
old_css_btn = """        .tactile-btn {
            transition: all 0.2s ease;
            position: relative;
        }
        .tactile-btn:hover {
            transform: translate(-2px, -2px);
            box-shadow: 2px 2px 0px 0px #C46231;
        }"""

new_css_btn = """        .tactile-btn {
            transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            will-change: transform;
        }
        .tactile-btn:hover {
            transform: translate(-2px, -2px);
            box-shadow: 3px 3px 0px 0px #C46231;
        }
        .tactile-btn:active {
            transform: scale(0.97) translate(0px, 0px) !important;
            box-shadow: 0px 0px 0px 0px #C46231 !important;
        }
        
        .product-card {
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform;
        }
        .product-card:hover {
            transform: scale(1.02);
        }
        .product-card:active {
            transform: scale(0.98);
        }
        
        /* Lightbox transitions */
        .lightbox-anim {
            transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        a, button {
            transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1) !important;
            transition-duration: 0.2s !important;
        }
        
        .active-scale:active {
            transform: scale(0.97) !important;
        }"""
html = html.replace(old_css_btn, new_css_btn)

# Remove old product-card CSS
old_product_card_css = """        .product-card {
            transition: transform 0.3s ease;
        }
        .product-card:hover {
            transform: scale(1.02);
        }
        .product-card:hover .product-img {
            transform: scale(1.05);
        }"""
html = html.replace(old_product_card_css, "")

# 2. Fix transition utility classes across HTML
html = html.replace('transition-colors duration-300', 'transition-colors')
html = html.replace('transition-all duration-300', 'transition-all')
html = html.replace('transition-all duration-200 ease-in-out', 'transition-colors hover:-translate-y-0.5 active:scale-95 inline-block')

# 3. Add tactile feedback to other buttons
# Lightbox Whatsapp button
old_wa = 'hover:bg-deep-teal transition-all text-lg"'
new_wa = 'hover:bg-deep-teal transition-all text-lg active-scale"'
html = html.replace(old_wa, new_wa)

# Close lightbox button
old_close = 'hover:text-terracotta transition-colors"'
new_close = 'hover:text-terracotta transition-colors active-scale"'
html = html.replace(old_close, new_close)

# 4. Bump Lightbox backdrop blur
html = html.replace('backdrop-blur-sm', 'backdrop-blur-md')

# 5. Fix form input focus states to be premium
old_input = 'type="text" placeholder="¿Cómo te llamas?"'
new_input = 'type="text" placeholder="¿Cómo te llamas?" class="w-full px-4 py-3 rounded-md border border-gray-300 focus:border-terracotta focus:ring-1 focus:ring-terracotta outline-none transition-all"'
if old_input in html:
    html = html.replace(old_input, new_input)
# The inputs are not in index.html (they might be in other pages, but we only have index.html open)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied Emil Kowalski principles and refined spacing!")
