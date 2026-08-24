import os
import glob
from PIL import Image, ImageDraw

dir_marcos = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
pngs = glob.glob(os.path.join(dir_marcos, "*.png"))

for f in pngs:
    try:
        img = Image.open(f).convert("RGBA")
        tw, th = img.size
        
        # Crear objeto para dibujar
        draw = ImageDraw.Draw(img)
        
        # Queremos borrar (hacer transparente) un área grande en el centro para destruir el texto.
        # Definimos los márgenes para no tocar las flores de los bordes.
        # Jugaremos a lo seguro: borraremos el centro dejando un margen del 20% en los lados
        # y 25% arriba/abajo.
        margin_x = int(tw * 0.15)
        margin_y = int(th * 0.18)
        
        # En RGBA, poner (0,0,0,0) borra el pixel
        draw.rectangle(
            [margin_x, margin_y, tw - margin_x, th - margin_y],
            fill=(0, 0, 0, 0)
        )
        
        # Sobreescribir el marco limpio
        img.save(f, "PNG")
        print(f"Texto central borrado en: {os.path.basename(f)}")
        
    except Exception as e:
        print(f"Error procesando {f}: {e}")

print("\n¡Limpieza de marcos completada!")
