import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the text/icon logo with the image logo in the navbar
old_logo = '''<span class="material-symbols-outlined text-primary text-3xl">bakery_dining</span>
<span class="font-display-lg text-headline-md text-primary tracking-tight">Glassitas</span>'''

new_logo = '''<img src="../assets/logo/logo_transparente.png" alt="Glassitas Logo" class="h-16 w-auto object-contain hover:scale-105 transition-transform">'''

html = html.replace(old_logo, new_logo)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Navbar logo fixed!")
