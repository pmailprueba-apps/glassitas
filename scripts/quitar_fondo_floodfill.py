import os, glob
from PIL import Image

def flood_fill_transparent(img_path):
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    # Get the background color from top-left corner
    bg_color = pixels[0, 0]
    
    # Tolerancia para variaciones del fondo (e.g. compresión JPEG)
    tolerance = 25
    
    def match(c1, c2):
        return (abs(c1[0]-c2[0]) < tolerance and 
                abs(c1[1]-c2[1]) < tolerance and 
                abs(c1[2]-c2[2]) < tolerance)
    
    # Set to keep track of visited pixels
    visited = set()
    
    # Cola para BFS
    queue = [(0, 0)]
    
    while queue:
        x, y = queue.pop(0)
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        
        if match(pixels[x, y], bg_color):
            pixels[x, y] = (255, 255, 255, 0)
            
            # Add neighbors
            if x > 0: queue.append((x-1, y))
            if x < width - 1: queue.append((x+1, y))
            if y > 0: queue.append((x, y-1))
            if y < height - 1: queue.append((x, y+1))

    img.save(img_path, "PNG")
    print(f"Fondo removido (FloodFill) en: {os.path.basename(img_path)}")

dir_path = "/Volumes/MiDisco1TB/Proyectos/44-glassitas/assets/logo/escaletas"
png_files = glob.glob(os.path.join(dir_path, "*.png"))

for f in png_files:
    try:
        print(f"Procesando {f}...")
        flood_fill_transparent(f)
    except Exception as e:
        print(f"Error procesando {f}: {e}")
