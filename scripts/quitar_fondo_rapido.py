import os, glob
from PIL import Image, ImageDraw

def process_frame(img_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    
    # We will flood fill with a unique magic color, then convert that color to transparent.
    # This prevents issues with thresholding replacing actual frame pixels.
    magic_color = (255, 0, 255, 255) # Magenta puro
    
    # Hacer flood fill desde las 4 esquinas y desde el centro
    # ImageDraw.floodfill muta la imagen en el lugar
    points = [
        (0, 0),
        (w-1, 0),
        (0, h-1),
        (w-1, h-1),
        (w//2, h//2)
    ]
    
    for pt in points:
        # Check if the pixel is close to white/gray before flooding
        pix = img.getpixel(pt)
        if pix[0] > 200 and pix[1] > 200 and pix[2] > 200:
            ImageDraw.floodfill(img, xy=pt, value=magic_color, thresh=30)
            
    # Ahora convertimos el color mágico a transparente
    datas = img.getdata()
    newData = []
    for item in datas:
        if item == magic_color:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(img_path, "PNG")
    print(f"Borde transparente rápido aplicado a: {os.path.basename(img_path)}")

dir_path = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
png_files = glob.glob(os.path.join(dir_path, "*.png"))

for f in png_files:
    try:
        process_frame(f)
    except Exception as e:
        print(f"Error procesando {f}: {e}")
