import os
import glob
from PIL import Image

# Rutas de entrada y salida
base_optimizados = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/optimizados"
base_marcos = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
base_salida = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/productos/con_marco"

# Mapeo de cuál marco usar para qué formato
# Clave: nombre de la carpeta optimizada, Valor: archivo de marco correspondiente
mapeo_marcos = {
    "1_1_Cuadrado_1080x1080": "escaleta insta.png", # Asumimos cuadrado/feed
    "4_5_Vertical_1080x1350": "escaleta vertical.png",
    "9_16_Historias_1080x1920": "escaleta tik tok .png",
    "191_1_Horizontal_1200x630": "escaleta hoizontal .png"
}

os.makedirs(base_salida, exist_ok=True)

# Cargamos los marcos en memoria para no leerlos cada vez
marcos_cargados = {}
for carpeta, archivo_marco in mapeo_marcos.items():
    ruta_marco = os.path.join(base_marcos, archivo_marco)
    if os.path.exists(ruta_marco):
        marcos_cargados[carpeta] = Image.open(ruta_marco).convert("RGBA")
    else:
        print(f"Advertencia: No se encontró el marco {ruta_marco}")

total_procesadas = 0

for carpeta, marco_img in marcos_cargados.items():
    ruta_carpeta_img = os.path.join(base_optimizados, carpeta)
    ruta_salida_carpeta = os.path.join(base_salida, carpeta)
    os.makedirs(ruta_salida_carpeta, exist_ok=True)
    
    imagenes = glob.glob(os.path.join(ruta_carpeta_img, "*.jpg"))
    if not imagenes:
        continue
        
    print(f"\n--- Aplicando marco a formato {carpeta} ({len(imagenes)} imágenes) ---")
    
    for img_path in imagenes:
        try:
            # 1. Abrir la imagen del producto (fondo)
            producto = Image.open(img_path).convert("RGBA")
            target_w, target_h = producto.size
            
            # 2. Ajustar el marco al tamaño exacto de la imagen
            # Hacemos un resize del marco para que encaje perfecto en el lienzo
            marco_redimensionado = marco_img.resize((target_w, target_h), Image.LANCZOS)
            
            # 3. Componer: Poner el marco sobre el producto
            # Se asume que el marco tiene el centro transparente
            resultado = Image.alpha_composite(producto, marco_redimensionado)
            
            # 4. Guardar resultado final
            base_name = os.path.basename(img_path)
            out_path = os.path.join(ruta_salida_carpeta, base_name)
            
            # Convertimos a RGB para guardarlo como JPG de alta calidad y bajo peso
            resultado.convert("RGB").save(out_path, "JPEG", quality=95)
            total_procesadas += 1
            
        except Exception as e:
            print(f"Error procesando {img_path}: {e}")

print(f"\n¡Listo! Se han generado {total_procesadas} imágenes con su marco correctamente superpuesto.")
print(f"Puedes verlas en: {base_salida}")
