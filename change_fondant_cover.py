import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the cover image for fondant-personalizadas
old_foto = r"(id: 'fondant-personalizadas'.*?foto:\s*'\.\./assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/)0047ac48-1662-4bcc-88b1-e547cdc92e8e\.jpg"
new_foto = r"\g<1>02ccee75-86e6-4cc2-8073-1cf83f97864f.jpg"
html = re.sub(old_foto, new_foto, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
