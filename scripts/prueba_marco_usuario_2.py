import os
from PIL import Image, ImageDraw

FRAME_PATH = "assets/logo/escaleta.png"
SAMPLE_PHOTO = "contenido/fotos reales de galletas/0047ac48-1662-4bcc-88b1-e547cdc92e8e.JPG"
OUTPUT_PATH = "assets/posts/facebook/prueba_marco_usuario_2.png"

def test_user_frame_2():
    target_size = (1080, 1080)
    
    # 1. Crear canvas con fondo gris claro
    canvas = Image.new("RGBA", target_size, "#EAEAEA")
    
    # 2. Cargar y procesar la foto (tira vertical)
    photo = Image.open(SAMPLE_PHOTO).convert("RGBA")
    
    # Queremos que la foto sea una tira vertical en el centro (ej: 540x1080)
    strip_w = 600
    strip_h = 1080
    
    p_width, p_height = photo.size
    # Hacer crop central de la foto original para que tenga proporción strip_w : strip_h
    aspect = strip_w / strip_h
    
    if p_width / p_height > aspect:
        # Foto es más ancha de lo necesario, recortar lados
        new_w = int(p_height * aspect)
        left = (p_width - new_w) / 2
        photo = photo.crop((left, 0, left + new_w, p_height))
    else:
        # Foto es más alta, recortar arriba/abajo
        new_h = int(p_width / aspect)
        top = (p_height - new_h) / 2
        photo = photo.crop((0, top, p_width, top + new_h))
        
    photo = photo.resize((strip_w, strip_h), Image.LANCZOS)
    
    # Posición central para la foto
    x_photo = (1080 - strip_w) // 2
    y_photo = 0
    
    # Pegar foto al canvas
    canvas.paste(photo, (x_photo, y_photo))
    
    # 3. Dibujar las líneas verdes a los lados de la foto (como en el mockup)
    draw = ImageDraw.Draw(canvas)
    line_width = 15
    green_color = "#1D4222" # Verde oscuro
    
    # Línea izquierda
    draw.rectangle([x_photo - line_width, 0, x_photo, target_size[1]], fill=green_color)
    # Línea derecha
    draw.rectangle([x_photo + strip_w, 0, x_photo + strip_w + line_width, target_size[1]], fill=green_color)
    
    # 4. Cargar y redimensionar el marco
    frame = Image.open(FRAME_PATH).convert("RGBA")
    # En el mockup el marco parece un poco aplastado para encajar, lo forzaremos a 1080 x 850 aprox.
    frame = frame.resize((1080, 850), Image.LANCZOS)
    
    x_frame = 0
    y_frame = (1080 - 850) // 2
    
    # Pegar el marco encima de todo
    canvas.paste(frame, (x_frame, y_frame), frame)
    
    # 5. Guardar
    canvas.convert("RGB").save(OUTPUT_PATH, quality=95)
    print(f"✅ Prueba guardada en: {OUTPUT_PATH}")

if __name__ == "__main__":
    test_user_frame_2()
