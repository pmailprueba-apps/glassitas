import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Horizontal folder with Cuadrado folder
html = html.replace('191_1_Horizontal_1200x630', '1_1_Cuadrado_1080x1080')

# Fix grid card aspect ratio
old_grid = '<div class="relative w-full  rounded-sm overflow-hidden ambient-shadow mb-6">'
new_grid = '<div class="relative w-full rounded-sm overflow-hidden ambient-shadow mb-6" style="aspect-ratio: 1/1;">'
html = html.replace(old_grid, new_grid)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Grid fixed!")
