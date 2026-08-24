import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_row = r'<tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">5\.0 cm</td><td class="p-4">\$23</td></tr>'
new_row = r'<tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">5.0 cm</td><td class="p-4">$23</td><td class="p-4">$22</td></tr>'

html = re.sub(old_row, new_row, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
