import re

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change Hero Image
hero_regex = r'<img alt="Galletas Decoradas Glassitas"[^>]*src="\.\./assets/productos/web/[^"]+"'
hero_new = '<img alt="Galletas Decoradas Glassitas" class="w-full h-full object-cover product-img" src="../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/31026464-65ed-4d2c-919d-c1ed6fb72773.jpg"'
html = re.sub(hero_regex, hero_new, html)

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated Hero Image")
