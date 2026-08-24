import re

faq_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html'
index_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'

with open(faq_path, 'r', encoding='utf-8') as f:
    faq_html = f.read()

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace fonts Google Fonts link in FAQ
old_fonts = r'<link href="https://fonts.googleapis.com/css2\?family=DM\+Sans.*?rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600&family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">'
faq_html = re.sub(old_fonts, new_fonts, faq_html)

# Add Tailwind Script from index if missing
tailwind_script = '<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>\n<script>\n'
# Get tailwind config from index
tw_config = re.search(r'(tailwind\.config = \{.*?\});', index_html, re.DOTALL)
if tw_config:
    tailwind_script += tw_config.group(1) + ';\n</script>'

if 'cdn.tailwindcss.com' not in faq_html:
    faq_html = faq_html.replace('</title>', '</title>\n' + tailwind_script)

# Homologate CSS font declarations inside <style>
faq_html = faq_html.replace("font-family:'DM Sans',sans-serif;", "font-family: 'Plus Jakarta Sans', sans-serif;")
faq_html = faq_html.replace("font-family:'Playfair Display',serif;", "font-family: 'Outfit', sans-serif;")
faq_html = faq_html.replace("font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;", "font-family: 'Plus Jakarta Sans', sans-serif;")

# 2. Extract Header (Navbar) from Index
header_match = re.search(r'(<header.*?</header>)', index_html, re.DOTALL)
if header_match:
    index_header = header_match.group(1)
    # Fix paths
    index_header = index_header.replace('../assets/', 'assets/')
    index_header = index_header.replace('href="#', 'href="nueva_web_pruebas/index.html#')
    index_header = index_header.replace('href="../preguntas-frecuentes.html"', 'href="#"')
    
    # Replace FAQ nav
    faq_html = re.sub(r'<nav>.*?</nav>', index_header, faq_html, flags=re.DOTALL)

# 3. Extract Footer from Index
footer_match = re.search(r'(<footer.*?</footer>)', index_html, re.DOTALL)
if footer_match:
    index_footer = footer_match.group(1)
    # Fix paths
    index_footer = index_footer.replace('../assets/', 'assets/')
    index_footer = index_footer.replace('href="#', 'href="nueva_web_pruebas/index.html#')
    index_footer = index_footer.replace('href="../preguntas-frecuentes.html"', 'href="#"')
    
    # Replace FAQ footer
    faq_html = re.sub(r'<footer>.*?</footer>', index_footer, faq_html, flags=re.DOTALL)


# Inject .btn-premium into FAQ CSS if missing
if '.btn-premium' not in faq_html:
    btn_premium_css = """
        .btn-premium {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background-color: #004B4D;
            color: #ffffff;
            padding: 1rem 2rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform;
            text-decoration: none;
        }
        .btn-premium:hover {
            background-color: #00383a;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            transform: translateY(-2px);
        }
        .btn-premium:active {
            transform: scale(0.97) translateY(0);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
"""
    faq_html = faq_html.replace('</style>', btn_premium_css + '\n</style>')

with open(faq_path, 'w', encoding='utf-8') as f:
    f.write(faq_html)
print("FAQ homologation complete!")
