import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

LOGO_PATH = "assets/logo/Gemini_Generated_Image_z0japzz0japzz0ja.png"
SAMPLE_BG = "contenido/fotos reales de galletas/IMG_6047.JPG"
OUTPUT_PATH = "assets/posts/facebook/prueba_escaleta_premium.jpg"
PHONE_TEXT = "WHATSAPP  •  +52 4445 101 553"

def rounded_rectangle_mask(size, radius):
    """Genera una máscara de bordes ultra redondeados (Píldora)."""
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask

def draw_text_with_tracking(draw, text, font, x, y, fill, tracking=2):
    """Dibuja texto con espacio entre letras (tracking)."""
    current_x = x
    for char in text:
        draw.text((current_x, y), char, font=font, fill=fill)
        bbox = font.getbbox(char)
        char_width = bbox[2] - bbox[0]
        current_x += char_width + tracking

def get_text_width(text, font, tracking):
    """Calcula el ancho total con tracking."""
    total_w = 0
    for char in text:
        bbox = font.getbbox(char)
        total_w += (bbox[2] - bbox[0]) + tracking
    return total_w - tracking

def apply_glass_pill(img):
    target_w, target_h = img.size
    
    # Dimensiones de la píldora
    pill_w = 800
    pill_h = 100
    pill_radius = 50
    x_pos = (target_w - pill_w) // 2
    # Colocar flotando en la parte superior (como pidió en la encuesta anterior)
    y_pos = 60
    
    # 1. Crear el área de cristal aislando esa región
    box = (x_pos, y_pos, x_pos + pill_w, y_pos + pill_h)
    glass_region = img.crop(box)
    
    # 2. Desenfoque profundo (Blur)
    glass_region = glass_region.filter(ImageFilter.GaussianBlur(radius=35))
    
    # 3. Capa translúcida para fusionar (OLED Black semi-transparente)
    dark_overlay = Image.new("RGBA", (pill_w, pill_h), (0, 0, 0, 160))
    glass_region = glass_region.convert("RGBA")
    glass_region = Image.alpha_composite(glass_region, dark_overlay)
    
    # 4. Máscara de Píldora
    mask = rounded_rectangle_mask((pill_w, pill_h), pill_radius)
    
    # 5. Pegar la píldora de cristal sobre la imagen final
    res = img.convert("RGBA")
    res.paste(glass_region, (x_pos, y_pos), mask)
    
    # 6. Borde físico brillante (Doble Bezel / Hairline)
    draw = ImageDraw.Draw(res)
    draw.rounded_rectangle((x_pos, y_pos, x_pos + pill_w, y_pos + pill_h), 
                           radius=pill_radius, outline=(255, 255, 255, 40), width=2)
    
    # 7. Integrar el Logo de forma sutil
    logo_h = 60
    padding = 20
    try:
        logo = Image.open(LOGO_PATH).convert("RGBA")
        aspect = logo.width / logo.height
        logo_w = int(logo_h * aspect)
        logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
        
        # Posición del logo dentro de la píldora
        logo_x = x_pos + padding + 10
        logo_y = y_pos + (pill_h - logo_h) // 2
        res.paste(logo, (logo_x, logo_y), logo)
    except Exception as e:
        print(f"Error cargando logo: {e}")
        logo_w = 0
        logo_x = x_pos
        
    # 8. Tipografía Editorial
    # Buscar una fuente premium del sistema. Helvetica es universal en Mac.
    font_path = "/System/Library/Fonts/Helvetica.ttc"
    if not os.path.exists(font_path):
        font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
        
    font = ImageFont.truetype(font_path, 28)
    tracking = 4
    
    text_w = get_text_width(PHONE_TEXT, font, tracking)
    # Centrar el texto en el espacio restante de la píldora
    space_left = pill_w - (logo_x - x_pos + logo_w)
    x_text = logo_x + logo_w + (space_left - text_w) // 2
    
    # Ajuste manual vertical para centrar el texto
    bbox = font.getbbox("A")
    text_h = bbox[3] - bbox[1]
    y_text = y_pos + (pill_h - text_h) // 2 - 4
    
    draw_text_with_tracking(draw, PHONE_TEXT, font, x_text, y_text, (255, 255, 255, 240), tracking=tracking)
    
    return res.convert('RGB')

if __name__ == "__main__":
    print("Generando The Glass Pill (Ultra Premium)...")
    
    # Usar una imagen de prueba
    if os.path.exists(SAMPLE_BG):
        bg = Image.open(SAMPLE_BG).convert("RGB")
        w, h = bg.size
        min_dim = min(w, h)
        left = (w - min_dim) / 2
        top = (h - min_dim) / 2
        bg = bg.crop((left, top, left+min_dim, top+min_dim)).resize((1080, 1080), Image.LANCZOS)
    else:
        bg = Image.new("RGB", (1080, 1080), (100, 100, 100))
        
    final = apply_glass_pill(bg)
    final.save(OUTPUT_PATH, quality=95)
    print(f"✅ Prueba guardada en: {OUTPUT_PATH}")
