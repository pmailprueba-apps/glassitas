import sys
from PIL import Image, ImageDraw

def make_circle_logo(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Hacer que la imagen sea perfectamente cuadrada (recortando el centro si no lo es)
    w, h = img.size
    min_dim = min(w, h)
    left = (w - min_dim)/2
    top = (h - min_dim)/2
    img = img.crop((left, top, left+min_dim, top+min_dim))
    
    # Crear máscara circular suave (antialias)
    mask = Image.new('L', (min_dim, min_dim), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, min_dim, min_dim), fill=255)
    
    # Aplicar la máscara al logo
    result = Image.new('RGBA', (min_dim, min_dim), (0,0,0,0))
    result.paste(img, (0,0), mask)
    
    result.save(output_path)
    print(f"Logo circular guardado en {output_path}")

make_circle_logo("assets/logo/Gemini_Generated_Image_z0japzz0japzz0ja.png", "assets/logo/logo_transparente.png")
