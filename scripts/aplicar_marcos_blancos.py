import os
import glob
from PIL import Image, ImageDraw

base_optimizados = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/optimizados"
base_marcos = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
base_salida = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/con_marco_blanco"

mapeo_marcos = {
    "1_1_Cuadrado_1080x1080": "escaleta insta.png",
    "4_5_Vertical_1080x1350": "escaleta vertical.png",
    "9_16_Historias_1080x1920": "escaleta tik tok .png",
    "191_1_Horizontal_1200x630": "escaleta hoizontal .png"
}

os.makedirs(base_salida, exist_ok=True)
marcos_cargados = {}
for carpeta, archivo_marco in mapeo_marcos.items():
    ruta = os.path.join(base_marcos, archivo_marco)
    if os.path.exists(ruta):
        marcos_cargados[carpeta] = Image.open(ruta).convert("RGBA")

total_procesadas = 0

for carpeta, marco_img in marcos_cargados.items():
    ruta_carpeta_img = os.path.join(base_optimizados, carpeta)
    ruta_salida_carpeta = os.path.join(base_salida, carpeta)
    os.makedirs(ruta_salida_carpeta, exist_ok=True)
    
    imagenes = glob.glob(os.path.join(ruta_carpeta_img, "*.jpg"))
    if not imagenes: continue
        
    print(f"\n--- Aplicando marco BLANCO a formato {carpeta} ({len(imagenes)} imgs) ---")
    
    for img_path in imagenes:
        try:
            producto = Image.open(img_path).convert("RGBA")
            tw, th = producto.size
            
            # Crear una capa blanca
            capa_blanca = Image.new("RGBA", (tw, th), (255, 255, 255, 255))
            mask = Image.new("L", (tw, th), 255) # 255 = blanco (opaco)
            draw = ImageDraw.Draw(mask)
            
            # Definir márgenes para el "hueco" (donde se verá el producto)
            # El marco floral suele ocupar un 10-15% del borde
            margin_x = int(tw * 0.12)
            margin_y = int(th * 0.12)
            
            # Dibujar un rectángulo redondeado negro (transparente) en la máscara
            # Esto hará un agujero en la capa blanca
            radius = int(min(tw, th) * 0.15)
            draw.rounded_rectangle(
                [margin_x, margin_y, tw - margin_x, th - margin_y],
                radius=radius, fill=0
            )
            
            # Aplicar la máscara a la capa blanca
            capa_blanca.putalpha(mask)
            
            # 1. Pegar la capa blanca hueca sobre el producto
            producto_con_borde_blanco = Image.alpha_composite(producto, capa_blanca)
            
            # 2. Pegar el marco floral encima de todo
            marco_redimensionado = marco_img.resize((tw, th), Image.LANCZOS)
            resultado = Image.alpha_composite(producto_con_borde_blanco, marco_redimensionado)
            
            out_path = os.path.join(ruta_salida_carpeta, os.path.basename(img_path))
            resultado.convert("RGB").save(out_path, "JPEG", quality=95)
            total_procesadas += 1
            
        except Exception as e:
            print(f"Error procesando {img_path}: {e}")

print(f"\n¡Listo! Generadas {total_procesadas} imágenes con exterior blanco y marco floral.")
