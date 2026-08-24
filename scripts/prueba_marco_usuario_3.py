import os
from PIL import Image

FRAME_PATH = "assets/logo/escaleta.png"
SAMPLE_PHOTO = "contenido/fotos reales de galletas/0047ac48-1662-4bcc-88b1-e547cdc92e8e.JPG"
OUTPUT_PATH = "assets/posts/facebook/prueba_marco_usuario_3.png"

def test_user_frame_3():
    # Queremos una imagen final cuadrada perfecta para Facebook (1080x1080)
    target_size = (1080, 1080)
    
    # 1. Cargar el marco y recortar TODO el espacio transparente exterior (Bounding Box)
    frame = Image.open(FRAME_PATH).convert("RGBA")
    bbox = frame.getbbox()
    if bbox:
        frame = frame.crop(bbox)
        
    # 2. Forzar el marco al tamaño de la imagen final (para que sea el borde absoluto)
    frame = frame.resize(target_size, Image.LANCZOS)
    
    # 3. Cargar la foto real de la galleta y hacerla cuadrada sin distorsionar
    photo = Image.open(SAMPLE_PHOTO).convert("RGBA")
    p_width, p_height = photo.size
    min_dim = min(p_width, p_height)
    left = (p_width - min_dim) / 2
    top = (p_height - min_dim) / 2
    photo = photo.crop((left, top, left + min_dim, top + min_dim))
    photo = photo.resize(target_size, Image.LANCZOS)
    
    # 4. Ensamblar: La foto es el fondo, el marco va exactamente encima, de borde a borde
    canvas = Image.new("RGBA", target_size)
    canvas.paste(photo, (0, 0))
    canvas.paste(frame, (0, 0), frame) # Usar el marco como máscara de transparencia
    
    # 5. Guardar
    canvas.convert("RGB").save(OUTPUT_PATH, quality=95)
    print(f"✅ Prueba guardada en: {OUTPUT_PATH}")

if __name__ == "__main__":
    test_user_frame_3()
