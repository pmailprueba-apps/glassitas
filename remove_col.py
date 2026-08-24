import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove TH
html = html.replace('<th class="p-4 font-semibold">1000+ unidades</th>\n', '')
html = html.replace('<th class="p-4 font-semibold">1000+ unidades</th>', '')

# Remove last TDs for the 1000+ column
rows_to_fix = [
    (r'<td class="p-4">\$16</td></tr>', '</tr>'),
    (r'<td class="p-4">\$21</td></tr>', '</tr>'),
    (r'<td class="p-4">\$36</td></tr>', '</tr>'),
    (r'<td class="p-4">\$41</td></tr>', '</tr>'),
    (r'<td class="p-4">\$22</td></tr>', '</tr>'),
    (r'<td class="p-4">\$32</td></tr>', '</tr>'),
]
for old, new in rows_to_fix:
    html = re.sub(old, new, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Column removed")
