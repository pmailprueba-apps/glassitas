import os
from PIL import Image

FRAME_PATH = "assets/logo/escaleta.png"
SAMPLE_PHOTO = "contenido/fotos reales de galletas/IMG_6047.JPG"
OUTPUT_PATH = "assets/posts/facebook/prueba_marco_usuario.png"

def test_user_frame():
    # Queremos una imagen final cuadrada perfecta para redes (1080x1080)
    target_size = (1080, 1080)
    
    # 1. Cargar y forzar el marco al tamaño objetivo (se ajustará para encajar perfecto)
    frame = Image.open(FRAME_PATH).convert("RGBA")
    frame = frame.resize(target_size, Image.LANCZOS)
    
    # 2. Cargar la foto real de la galleta
    photo = Image.open("contenido/fotos reales de galletas/0047ac48-1662-4bcc-88b1-e547cdc92e8e.JPG").convert("RGBA")
    
    # 3. Recortar la foto para que sea cuadrada (1:1) sin distorsionarla, enfocando el centro
    p_width, p_height = photo.size
    min_dim = min(p_width, p_height)
    left = (p_width - min_dim) / 2
    top = (p_height - min_dim) / 2
    photo = photo.crop((left, top, left + min_dim, top + min_dim))
    
    # 4. Redimensionar la foto cuadrada al tamaño objetivo
    photo = photo.resize(target_size, Image.LANCZOS)
    
    # 5. Crear el canvas y ensamblar
    canvas = Image.new("RGBA", target_size)
    canvas.paste(photo, (0, 0))
    canvas.paste(frame, (0, 0), frame) # Usar el marco como máscara de transparencia
    
    # 4. Guardar
    canvas.save(OUTPUT_PATH)
    print(f"✅ Prueba guardada en: {OUTPUT_PATH}")

if __name__ == "__main__":
    test_user_frame()
