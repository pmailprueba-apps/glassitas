import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

IMG_DIR = "contenido/fotos reales de galletas"
OUTPUT_DIR = "assets/posts/facebook"
os.makedirs(OUTPUT_DIR, exist_ok=True)

LOGO_PATH = "assets/logo/logo_transparente.png"
FRAME_PATH = "assets/logo/escaleta.png"
PHONE_TEXT = "WHATSAPP  +52 4445 101 553"

# Formato 16:9 (1080x608) para respetar el marco floral horizontal sin distorsión
TARGET_W, TARGET_H = 1080, 608

FB_DATA = [
    {
        "nombre": "fb_1_bodas",
        "textos": [
            "DETALLES PREMIUM PARA TU BODA",
            "RECUERDOS COMESTIBLES",
            "COTIZA TU EVENTO AHORA"
        ]
    },
    {
        "nombre": "fb_2_babyshower",
        "textos": [
            "EL BABY SHOWER PERFECTO",
            "GALLETAS DE MANTEQUILLA",
            "RESERVA TU FECHA AQUÍ"
        ]
    },
    {
        "nombre": "fb_3_infantil",
        "textos": [
            "DISEÑOS ÚNICOS PARA FIESTAS",
            "SU PERSONAJE FAVORITO",
            "COTIZA TU TEMÁTICA"
        ]
    }
]

valid_exts = (".jpg", ".jpeg", ".png")
all_images = [f for f in os.listdir(IMG_DIR) if f.lower().endswith(valid_exts)]


def load_frame_cover(target_w, target_h):
    """Carga el marco floral y lo escala en modo 'cover' sin distorsión,
    recortando solo un mínimo del exceso para que sea el borde absoluto."""
    frame = Image.open(FRAME_PATH).convert("RGBA")
    fw, fh = frame.size
    scale = max(target_w / fw, target_h / fh)
    new_w, new_h = int(fw * scale), int(fh * scale)
    frame = frame.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    frame = frame.crop((left, top, left + target_w, top + target_h))
    return frame


def cover_crop(img, target_w, target_h):
    """Recorta la foto en modo cover al ratio objetivo sin distorsión."""
    width, height = img.size
    target_ratio = target_w / target_h
    current_ratio = width / height
    if current_ratio > target_ratio:
        new_w = int(height * target_ratio)
        left = (width - new_w) // 2
        return img.crop((left, 0, left + new_w, height))
    else:
        new_h = int(width / target_ratio)
        top = (height - new_h) // 2
        return img.crop((0, top, width, top + new_h))


def enhance_food(img):
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.18)
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.08)
    shar = ImageEnhance.Sharpness(img)
    img = shar.enhance(1.15)
    return img


def get_font(size):
    candidates = [
        "/System/Library/Fonts/Supplemental/Georgia.ttc",
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def add_bottom_gradient(img, target_h):
    """Degradado suave solo en la franja inferior para legibilidad del texto.
    Nada de bloques sólidos."""
    width, height = TARGET_W, TARGET_H
    gradient = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    fade_height = int(height * 0.5)
    for y in range(fade_height):
        yy = height - fade_height + y
        alpha = int(150 * (y / fade_height))
        draw.line([(0, yy), (width, yy)], fill=(0, 0, 0, alpha))
    res = Image.alpha_composite(img.convert("RGBA"), gradient)
    return res.convert("RGB")


def draw_text_tracking(draw, text, font, x, y, fill, tracking=3, shadow=True):
    current_x = x
    for char in text:
        if shadow:
            draw.text((current_x + 2, y + 2), char, font=font, fill=(0, 0, 0, 200))
        draw.text((current_x, y), char, font=font, fill=fill)
        bbox = font.getbbox(char)
        current_x += (bbox[2] - bbox[0]) + tracking


def text_width(text, font, tracking):
    total = 0
    for char in text:
        bbox = font.getbbox(char)
        total += (bbox[2] - bbox[0]) + tracking
    return total - tracking


def assemble(img_rgb, frame, main_text, is_cta):
    """Ensambla: foto como base, marco floral encima, logo y textos."""
    canvas = img_rgb.convert("RGBA")
    canvas.paste(frame, (0, 0), frame)

    draw = ImageDraw.Draw(canvas)
    padding = 44

    # ---- Logo (esquina inferior izquierda, discreto, fuera del centro) ----
    logo_size = 96
    x_logo = padding
    y_logo = TARGET_H - logo_size - padding
    try:
        logo = Image.open(LOGO_PATH).convert("RGBA")
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        shadow = Image.new("RGBA", (logo_size, logo_size))
        sd = ImageDraw.Draw(shadow)
        sd.ellipse((4, 4, logo_size - 4, logo_size - 4), fill=(0, 0, 0, 120))
        shadow = shadow.filter(ImageFilter.GaussianBlur(12))

        canvas.paste(shadow, (x_logo, y_logo + 6), shadow)
        canvas.paste(logo, (x_logo, y_logo), logo)
        draw = ImageDraw.Draw(canvas)
    except Exception as e:
        print("  (logo omitido)", e)

    # ---- Teléfono (a la derecha del logo, mismo eje) ----
    phone_font = get_font(20)
    phone_tracking = 2
    x_phone = x_logo + logo_size + 24
    y_phone = y_logo + (logo_size // 2) - 12
    draw_text_tracking(draw, PHONE_TEXT, phone_font, x_phone, y_phone,
                       (255, 255, 255, 230), tracking=phone_tracking)

    # ---- Texto principal (arriba izquierda) ----
    main_font = get_font(46)
    main_tracking = 4
    color = (240, 214, 160) if is_cta else (255, 255, 255)
    # Sombra de texto reforzada por encima (zona posiblemente clara)
    x_main = padding
    y_main = padding + 6

    # Pequeño escudo de legibilidad: sombra difuminada bajo el texto, sin bloque solido
    tw = text_width(main_text, main_font, main_tracking)
    th = 60
    shade = Image.new("RGBA", (280, 90), (0, 0, 0, 0))
    shd = ImageDraw.Draw(shade)
    shd.text((8, 8), main_text, font=main_font, fill=(0, 0, 0, 160))
    shade = shade.filter(ImageFilter.GaussianBlur(18))
    # solo expandimos un poco mas que el texto
    canvas.paste(shade, (x_main - 30, y_main - 28), shade)
    draw = ImageDraw.Draw(canvas)
    draw_text_tracking(draw, main_text, main_font, x_main, y_main,
                       color, tracking=main_tracking)

    return canvas.convert("RGB")


print("Generando banners 16:9 con marco floral (High-End)...")
frame = load_frame_cover(TARGET_W, TARGET_H)

for ad in FB_DATA:
    print(f"-> {ad['nombre']}")
    random.shuffle(all_images)
    selected = all_images[:3]
    for i, img_name in enumerate(selected):
        img_path = os.path.join(IMG_DIR, img_name)
        img = Image.open(img_path).convert("RGB")
        img = cover_crop(img, TARGET_W, TARGET_H)
        img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
        img = enhance_food(img)
        img = add_bottom_gradient(img, TARGET_H)

        is_cta = (i == 2)
        ad_img = assemble(img, frame, ad["textos"][i], is_cta=is_cta)

        out = os.path.join(OUTPUT_DIR, f"{ad['nombre']}_{i+1}.jpg")
        ad_img.save(out, quality=95)
        print(f"   OK {out} ({ad_img.size[0]}x{ad_img.size[1]})")

print("Listo: anuncios con marco floral generados.")
