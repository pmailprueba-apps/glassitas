import os
from PIL import Image, ImageDraw, ImageFont

LOGO_PATH = "assets/logo/logo-glassitas.png"
OUTPUT_DIR = "assets/productos/con-marca/"
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"

os.makedirs(OUTPUT_DIR, exist_ok=True)

logo = Image.open(LOGO_PATH).convert("RGBA")

# Resize logo to ~15% of image width
logo_max_w = 200
logo.thumbnail((logo_max_w, int(logo_max_w * logo.size[1] / logo.size[0])), Image.LANCZOS)

for fname in os.listdir("assets/productos"):
    if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        continue

    img = Image.open(f"assets/productos/{fname}").convert("RGBA")
    pad = 20
    x = img.width - logo.width - pad
    y = img.height - logo.height - pad

    if logo.mode == "RGBA":
        img.paste(logo, (x, y), logo)
    else:
        img.paste(logo, (x, y))

    out_path = os.path.join(OUTPUT_DIR, fname)
    img.convert("RGB").save(out_path, quality=95)
    print(f"✅ {fname} -> {out_path}")
