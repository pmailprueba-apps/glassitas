import re

html_path = '../preguntas-frecuentes.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_answer = "<p>No, somos fábrica especializada en galletas personalizadas.</p>"
new_answer = "<p>Sí, también hacemos pasteles y muffins personalizados.</p>"
html = html.replace(old_answer, new_answer)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("FAQ updated!")
