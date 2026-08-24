from PIL import Image, ImageOps
import os

def bake(base_path, frame_path, out_name):
    base_img = Image.open(base_path).convert("RGBA")
    frame = Image.open(frame_path).convert("RGBA")
    fitted_base = ImageOps.fit(base_img, frame.size, method=Image.Resampling.LANCZOS)
    final = Image.alpha_composite(fitted_base, frame)
    final.convert("RGB").save(out_name)
    print(f"Saved {out_name}")

# Variant 1: Horizontal (1200x630) + escaleta horizontal 2
bake(
    'assets/productos/con_marco_blanco/191_1_Horizontal_1200x630/0047ac48-1662-4bcc-88b1-e547cdc92e8e.jpg',
    'assets/logo/escaletas/escaleta horizontal 2.png',
    'test_horizontal.jpg'
)

# Variant 2: Square (1080x1080) + escaleta insta
bake(
    'assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0047ac48-1662-4bcc-88b1-e547cdc92e8e.jpg',
    'assets/logo/escaletas/escaleta insta.png',
    'test_square.jpg'
)

# Variant 3: Vertical (1080x1350) + escaleta vertical
bake(
    'assets/productos/con_marco_blanco/4_5_Vertical_1080x1350/0047ac48-1662-4bcc-88b1-e547cdc92e8e.jpg',
    'assets/logo/escaletas/escaleta vertical.png',
    'test_vertical.jpg'
)

