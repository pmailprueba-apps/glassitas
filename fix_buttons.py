import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the renderFormas loop output to ensure the layout matches the high-end rules
# We need to find the `renderFormas` function body
formas_match = re.search(r'function renderFormas\(\) \{.*?\}(?=\n\n\s+function)', html, re.DOTALL)
if formas_match:
    original_formas = formas_match.group(0)
    # the html generation looks like: `<button class="shape-btn ...
    new_formas = original_formas.replace('<button class="shape-btn ${activo} flex items-center justify-center gap-2 p-3 md:p-4 rounded-xl border border-gray-200 transition-all font-semibold"',
                                         '<button class="shape-btn ${activo} group flex items-center justify-center p-3 md:p-4 rounded-full border border-gray-200 transition-all duration-500 ease-[cubic-bezier(0.32,0.72,0,1)] hover:scale-[0.98] font-bold text-sm tracking-wide"')
    html = html.replace(original_formas, new_formas)
    
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
