import re

faq_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html'
index_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'

with open(faq_path, 'r', encoding='utf-8') as f:
    faq_html = f.read()

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# 1. Extract Head from Index (up to </style>)
head_match = re.search(r'(<head>.*?</style>)', index_html, re.DOTALL)
if head_match:
    index_head = head_match.group(1)
    # Fix paths in head for FAQ (FAQ is in root, index is in nueva_web_pruebas)
    index_head = index_head.replace('../assets/', 'assets/')
    
    # Replace FAQ head
    faq_html = re.sub(r'<head>.*?</style>', index_head, faq_html, flags=re.DOTALL)

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
    faq_html = re.sub(r'<footer.*?</script>', index_footer + '\n</body>\n</html>', faq_html, flags=re.DOTALL)

# 4. Homologate Fonts in the body of FAQ
faq_html = faq_html.replace("font-family:'DM Sans',sans-serif;", "font-family: 'Plus Jakarta Sans', sans-serif;")
faq_html = faq_html.replace("font-family:'Playfair Display',serif;", "font-family: 'Outfit', sans-serif;")
faq_html = faq_html.replace("font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;", "font-family: 'Plus Jakarta Sans', sans-serif;")

# Remove the old raw CSS custom properties to let Tailwind takeover where possible, or just keep them for the FAQ accordion.
# The old FAQ has inline <style> that I might have overwritten when I replaced the head. 
# WAIT. If I replace the entire <head> ... </style> block, I will delete the custom CSS for the FAQ accordion!
