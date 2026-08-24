import os
import random
from PIL import Image, ImageDraw, ImageFont

# Directorios
IMG_DIR = "contenido/fotos reales de galletas"
OUTPUT_DIR = "assets/posts/ads"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Copys de los anuncios (basados en la estrategia generada)
ADS_DATA = [
    {"angle": "1_contraste", "headline": "El recuerdo que nadie tirará.", "cta": "Cotiza tu diseño aquí >"},
    {"angle": "1_contraste", "headline": "Arte comestible para tu boda.", "cta": "Agenda tu fecha gratis >"},
    {"angle": "2_prueba_social", "headline": "Las favoritas en San Luis Potosí.", "cta": "Últimos lugares del mes >"},
    {"angle": "2_prueba_social", "headline": "Haz que tu evento destaque.", "cta": "Más de 500 clientes felices >"}
]

# Obtener imagenes
valid_exts = (".jpg", ".jpeg", ".png")
images = [f for f in os.listdir(IMG_DIR) if f.lower().endswith(valid_exts)]
random.shuffle(images)
selected_images = images[:4] # Tomar 4 fotos al azar

# Configuracion de fuente (Mac OS standard)
try:
    font_main = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 60)
    font_cta = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 35)
except:
    font_main = ImageFont.load_default()
    font_cta = ImageFont.load_default()

for i, ad in enumerate(ADS_DATA):
    if i >= len(selected_images):
        break
    
    img_path = os.path.join(IMG_DIR, selected_images[i])
    img = Image.open(img_path).convert("RGBA")
    
    # Recortar a 1080x1080 (1:1 Ratio para FB/IG)
    target_size = 1080
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    img = img.crop((left, top, right, bottom))
    img = img.resize((target_size, target_size), Image.LANCZOS)
    
    # Crear overlay negro con gradiente (simplificado a overlay semi-transparente en la parte inferior)
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle([0, int(target_size*0.65), target_size, target_size], fill=(0, 0, 0, 160))
    
    # Combinar img y overlay
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    # Escribir textos
    draw.text((50, target_size - 250), ad["headline"], font=font_main, fill=(255, 255, 255, 255))
    draw.text((50, target_size - 120), ad["cta"], font=font_cta, fill=(255, 215, 0, 255)) # Color dorado
    
    # Guardar
    out_name = f"ad_{ad['angle']}_{i+1}.jpg"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    img.convert("RGB").save(out_path, quality=95)
    print(f"Generado: {out_path}")

print("✅ Todos los artes (imágenes) de la campaña generados con éxito.")
