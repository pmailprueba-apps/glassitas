import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace custom pseudo-Material classes with standard Tailwind
replacements = {
    'font-body-lg': 'text-lg font-medium',
    'font-body-md': 'text-base',
    'font-display-lg': 'text-6xl font-bold font-serif', # Wait, font-serif is not defined, we used Outfit for h1, h2, h3 and .font-display
    'font-display-md': 'text-5xl font-bold font-serif',
    'font-headline-md': 'text-2xl font-bold',
    'font-headline-sm': 'text-xl font-medium',
    'font-label-caps': 'text-sm font-bold uppercase tracking-wider',
    'text-title-lg': 'text-xl font-semibold',
    'text-headline-md': 'text-2xl font-bold',
    'font-medium': 'font-medium'
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Also fix the specific section the user complained about
# <h2 class="text-3xl md:text-5xl text-primary font-bold tracking-tight mb-12 text-center text-center">Galletas de Diseño Personalizado</h2>
# <p class="text-lg font-medium text-on-surface-variant">Artesanía en cada detalle. Perfectas para bodas, bautizos y celebraciones únicas.</p>
# It needs to be styled better. Let's make it more premium.
old_subtitle = '<p class="text-lg font-medium text-on-surface-variant">Artesanía en cada detalle. Perfectas para bodas, bautizos y celebraciones únicas.</p>'
new_subtitle = '<p class="text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[65ch] mx-auto text-center mt-4 mb-16">Artesanía en cada detalle. Perfectas para bodas, bautizos y celebraciones únicas.</p>'
html = html.replace(old_subtitle, new_subtitle)

# And fix the duplicate text-center text-center on h2
html = html.replace('text-center text-center', 'text-center')

# Update card titles to be more prominent
# <h3 class="text-lg font-medium font-medium text-deep-teal mb-2 group-hover:text-terracotta transition-colors">${e.ico} ${e.nombre}</h3>
html = html.replace('text-lg font-medium font-medium text-deep-teal', 'text-xl font-semibold text-deep-teal')

# Remove duplicate font-medium that was created by the replace
html = html.replace('font-medium font-medium', 'font-medium')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Typography classes updated!")
