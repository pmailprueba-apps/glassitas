import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix foto and fotos for institucional
old_block = r"foto: REF_BASE \+ 'institucion/img_1\.jpg',\s*fotos: \['\.\./assets/productos/optimizados/web_con_escaleta/ba43b971-81d6-44c1-b56c-dd7684b2da51\.jpg', '\.\./assets/productos/optimizados/web_con_escaleta/c2d74894-7a4f-40ea-a427-6104894282a9\.jpg', '\.\./assets/productos/optimizados/web_con_escaleta/c6b6e3c2-1abe-4791-ba87-4f31ae54c489\.jpg', '\.\./assets/productos/optimizados/web_con_escaleta/d396adef-8139-4944-8bf9-017e7428cb51\.jpg'\],"

new_block = "foto: '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_1.jpg',\n        fotos: ['../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_1.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_2.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_3.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_4.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_5.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_6.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_7.jpg', '../assets/productos/con_marco_blanco/galerias_con_marco/institucion/img_8.jpg'],"

html = re.sub(old_block, new_block, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Institucional images fixed!")
