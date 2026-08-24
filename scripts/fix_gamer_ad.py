import os
from PIL import Image, ImageChops, ImageDraw, ImageFont

IMG_DIR = "contenido/fotos reales de galletas"
OUTPUT_DIR = "assets/posts/ads"
ad_target = Image.open(os.path.join(OUTPUT_DIR, "ad_1_contraste_2.jpg")).convert("RGB")
ad_target_crop = ad_target.crop((0, 0, 1080, 500)) # Top half without text

best_match = None
best_diff = 999999999

valid_exts = (".jpg", ".jpeg", ".png")
for fname in os.listdir(IMG_DIR):
    if not fname.lower().endswith(valid_exts): continue
    
    img_path = os.path.join(IMG_DIR, fname)
    img = Image.open(img_path).convert("RGBA")
    
    # Same crop logic
    target_size = 1080
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    img = img.crop((left, top, right, bottom))
    img = img.resize((target_size, target_size), Image.LANCZOS)
    img_rgb = img.convert("RGB")
    
    img_crop = img_rgb.crop((0, 0, 1080, 500))
    diff = ImageChops.difference(ad_target_crop, img_crop)
    # sum of differences
    colors = diff.getcolors(1080*500)
    diff_val = sum(count * sum(rgb) for count, rgb in colors) if colors else 999999999
    
    if diff_val < best_diff:
        best_diff = diff_val
        best_match = (fname, img)

print(f"Original image found: {best_match[0]} with diff {best_diff}")

# Now generate the new gamer ad
img = best_match[1]

overlay = Image.new('RGBA', img.size, (0,0,0,0))
draw = ImageDraw.Draw(overlay)
draw.rectangle([0, int(1080*0.65), 1080, 1080], fill=(0, 0, 0, 160))

img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

try:
    font_main = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 60)
    font_cta = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 35)
except:
    font_main = ImageFont.load_default()
    font_cta = ImageFont.load_default()

headline = "Sube de nivel la fiesta de tu hijo. 🍄"
cta = "Cotiza tu temática favorita >"

draw.text((50, 1080 - 250), headline, font=font_main, fill=(255, 255, 255, 255))
draw.text((50, 1080 - 120), cta, font=font_cta, fill=(255, 215, 0, 255))

out_path = os.path.join(OUTPUT_DIR, "ad_3_gamer_ninos.jpg")
img.convert("RGB").save(out_path, quality=95)
print(f"Generado nuevo arte gamer: {out_path}")

# Eliminar el de la boda
os.remove(os.path.join(OUTPUT_DIR, "ad_1_contraste_2.jpg"))
