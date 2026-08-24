import re
import os
import random

baked_dir = 'assets/productos/optimizados/web_con_escaleta'
baked_files = sorted([f for f in os.listdir(baked_dir) if f.endswith('.jpg')])

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove CSS frame-overlay logic entirely
html = re.sub(r'\$\{e\.has_frame \? \'\' : \'<div class="frame-overlay-vertical[^>]+></div>\'\}', '', html)
html = re.sub(r'\$\{e\.has_frame \? \'\' : \'<div class="frame-overlay-horizontal[^>]+></div>\'\}', '', html)
html = re.sub(r'\.product-card > \.relative\.thumb-container \{ aspect-ratio: 2816 / 1536; \}', '.product-card > .relative.thumb-container { aspect-ratio: 2816 / 1536; }', html) # keep aspect ratio

# 2. Update the REF_BASE, although we will use absolute relative paths now.
# We can just change all the foto and fotos fields.
# We have 8 categories to fill (excluding fondant which is index 0)
# Let's extract the EVENTOS array
eventos_match = re.search(r'const EVENTOS = \[(.*?)\];', html, re.DOTALL)
if eventos_match:
    eventos_content = eventos_match.group(1)
    # Split by {id:
    categories = re.split(r'(\{\s*id:)', eventos_content)
    # categories[0] is empty or whitespace
    # categories[1] is '{ id:'
    # categories[2] is the rest of the first object, etc.
    
    new_eventos = []
    baked_idx = 0
    for i in range(1, len(categories), 2):
        cat_str = categories[i] + categories[i+1]
        
        if 'fondant-personalizadas' in cat_str:
            new_eventos.append(cat_str)
            continue
            
        # Assign 4 baked images to this category
        cat_files = []
        for _ in range(4):
            if baked_idx < len(baked_files):
                cat_files.append(f"'../assets/productos/optimizados/web_con_escaleta/{baked_files[baked_idx]}'")
                baked_idx += 1
            else:
                cat_files.append(f"'../assets/productos/optimizados/web_con_escaleta/{baked_files[0]}'") # fallback
                
        # Update foto:
        cat_str = re.sub(r"foto:\s*'(.*?)',", f"foto: {cat_files[0]},", cat_str)
        # Update fotos:
        fotos_str = "[" + ", ".join(cat_files) + "]"
        cat_str = re.sub(r"fotos:\s*\[(.*?)\]", f"fotos: {fotos_str}", cat_str, flags=re.DOTALL)
        
        new_eventos.append(cat_str)

    new_eventos_str = "".join(new_eventos)
    html = html.replace(eventos_match.group(1), new_eventos_str)
    
# 3. Change REF_BASE in renderEventos to empty since we use absolute paths now
html = html.replace("const ejemplos = (e.fotos || []).map(f => f.startsWith('../') ? f : REF_BASE + f);", 
                    "const ejemplos = (e.fotos || []);")
html = html.replace("const imgUrl = f.startsWith('http') ? f : (e.foto ? e.foto : REF_BASE + f);",
                    "const imgUrl = e.foto;")


with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated index.html to use baked images directly without CSS overlays.")
