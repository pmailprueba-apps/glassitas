import sys
from PIL import Image, ImageDraw

def process_frame(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Queremos rellenar la parte exterior transparente con blanco.
    # El floodfill llenará todo lo que conecte con el píxel (0,0) que sea transparente.
    
    # Primero, necesitamos un blanco sólido.
    fill_color = (255, 255, 255, 255)
    
    # Hacemos floodfill desde las esquinas. Si el borde floral es cerrado, esto rellenará
    # solo el exterior.
    w, h = img.size
    corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
    
    # The floodfill will target exactly transparent pixels. But anti-aliased edges might have partial transparency.
    # To be safer, we can check alpha. But PIL's floodfill matches exact colors if no thresh.
    # Let's see what color the transparent pixels are (usually (0,0,0,0) or (255,255,255,0)).
    corner_pixel = img.getpixel((0,0))
    print(f"Color en (0,0): {corner_pixel}")
    
    # We can use a custom flood fill if PIL's is finicky with alpha.
    # Let's try PIL's ImageDraw.floodfill
    for corner in corners:
        if img.getpixel(corner)[3] < 10: # Si es transparente
            ImageDraw.floodfill(img, corner, fill_color, thresh=50)
            
    img.save(output_path, "PNG")
    print(f"Prueba guardada en: {output_path}")

process_frame("/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas/escaleta insta.png", "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas/prueba_exterior_blanco.png")
