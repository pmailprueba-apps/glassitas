import os
import random
import subprocess
import shutil
import math
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = "assets/productos/con_marco_blanco/9_16_Historias_1080x1920"
OUTPUT_DIR = "assets/posts/tiktok"
TEMP_DIR = "assets/posts/tiktok/temp"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

VIDEOS_DATA = [
    {
        "nombre": "tiktok_1_bodas",
        "textos": [
            "LO QUE NADIE TE DICE\nSOBRE LOS RECUERDOS",
            "EL 90% TERMINA\nEN LA BASURA",
            "REGALA ARTE COMESTIBLE.\nCOTIZA AQUÍ"
        ]
    },
    {
        "nombre": "tiktok_2_babyshower",
        "textos": [
            "MESA DE POSTRES\nNIVEL PREMIUM",
            "SIN GASTAR\nUNA FORTUNA",
            "RESERVA TU FECHA\nEN EL LINK"
        ]
    },
    {
        "nombre": "tiktok_3_slp",
        "textos": [
            "LAS GALLETAS MÁS PEDIDAS\nDE SAN LUIS POTOSÍ",
            "SABOR A MANTEQUILLA\nY DISEÑO IMPECABLE",
            "COTIZA TU EVENTO\nEN NUESTRO PERFIL"
        ]
    },
    {
        "nombre": "tiktok_4_infantil",
        "textos": [
            "¿BOLSITAS DE DULCES\nABURRIDAS?",
            "GALLETAS DE SU\nPERSONAJE FAVORITO",
            "COTIZA TU TEMÁTICA\nHOY MISMO"
        ]
    }
]

valid_exts = (".jpg", ".jpeg", ".png")
all_images = [f for f in os.listdir(IMG_DIR) if f.lower().endswith(valid_exts)]

def get_fitted_font(text_lines, max_width, max_height, start_size=120):
    font_path = os.path.expanduser("~/Library/Fonts/GoogleFonts/Anton-Regular.ttf")
    size = start_size
    while size > 30:
        try:
            font = ImageFont.truetype(font_path, size)
        except:
            font = ImageFont.load_default()
            return font
        max_w, total_h = 0, 0
        for line in text_lines:
            bbox = font.getbbox(line)
            w = bbox[2] - bbox[0]
            if w > max_w: max_w = w
            total_h += (font.size * 1.2)
        if max_w <= max_width and total_h <= max_height:
            return font
        size -= 5
    return font

def ease_out_back(t):
    """Función matemática para el rebote elástico (Pop-in)"""
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(t - 1, 3) + c1 * math.pow(t - 1, 2)

def draw_frame(bg_img, text_img, target_w, target_h, frame_idx, total_frames, clip_idx=0):
    # 1. Calcular animación del fondo (Ken Burns Dinámico)
    progress = frame_idx / total_frames
    
    if clip_idx == 0:
        # Movimiento 1: Zoom In suave
        zoom = 1.0 + (0.15 * progress)
        new_w = int(target_w / zoom)
        new_h = int(target_h / zoom)
        left = (target_w - new_w) / 2
        top = (target_h - new_h) / 2
    elif clip_idx == 1:
        # Movimiento 2: Pan Horizontal (Deslizamiento)
        # Hacemos un zoom fijo de 1.15 para tener margen de paneo
        zoom = 1.15
        new_w = int(target_w / zoom)
        new_h = int(target_h / zoom)
        # Deslizar de izquierda a derecha
        max_pan = target_w - new_w
        left = max_pan * progress
        top = (target_h - new_h) / 2
    else:
        # Movimiento 3: Zoom Out + Tilt Down (Deslizamiento vertical)
        zoom = 1.15 - (0.10 * progress)
        new_w = int(target_w / zoom)
        new_h = int(target_h / zoom)
        left = (target_w - new_w) / 2
        # Deslizar de arriba hacia abajo
        max_pan = target_h - new_h
        top = max_pan * (1 - progress)
        
    frame_bg = bg_img.crop((left, top, left + new_w, top + new_h))
    frame_bg = frame_bg.resize((target_w, target_h), Image.LANCZOS)
    
    # 2. Calcular animación del texto (Pop-in con rebote)
    # La animación dura los primeros 15 frames (0.5 segundos)
    anim_duration = 15
    if frame_idx < anim_duration:
        t = frame_idx / anim_duration
        scale = ease_out_back(t)
        # Fade in opacity (primeros 10 frames)
        alpha = min(255, int((frame_idx / 10) * 255))
    else:
        # Pequeño escalado continuo para que el texto no esté 100% estático (Respira)
        scale = 1.0 + (0.05 * progress)
        alpha = 255
        
    # Aplicar opacidad al texto
    if alpha < 255:
        txt_alpha = text_img.copy()
        txt_alpha.putalpha(txt_alpha.getchannel('A').point(lambda p: p * (alpha / 255.0)))
    else:
        txt_alpha = text_img
        
    # Aplicar escala al texto
    if scale > 0.01:
        new_txt_w = max(1, int(target_w * scale))
        new_txt_h = max(1, int(target_h * scale))
        # Resize using BICUBIC for better quality
        scaled_txt = txt_alpha.resize((new_txt_w, new_txt_h), Image.BICUBIC)
        # Calcular posición centrada
        paste_x = (target_w - new_txt_w) // 2
        paste_y = (target_h - new_txt_h) // 2
        frame_bg.paste(scaled_txt, (paste_x, paste_y), scaled_txt)
        
    return frame_bg

def create_transparent_text(text_lines, target_w, target_h, font, is_cta=False):
    img = Image.new('RGBA', (target_w, target_h), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    total_text_height = len(text_lines) * (font.size * 1.2)
    # Posicionar en el tercio inferior (Lower Third) para no tapar el centro, dejando margen para UI de TikTok
    y_text = 1450 - total_text_height 
    stroke_width = int(font.size * 0.1)
    
    for i, line in enumerate(text_lines):
        bbox = font.getbbox(line)
        w = bbox[2] - bbox[0]
        x_text = (target_w - w) / 2
        
        color = (255, 255, 255, 255)
        if is_cta and i == len(text_lines)-1:
             color = (255, 223, 0, 255) # Amarillo TikTok
             
        # Drop shadow & Stroke
        draw.text((x_text + stroke_width + 5, y_text + stroke_width + 5), line, font=font, fill=(0,0,0, 200))
        for adj_x in range(-stroke_width, stroke_width+1):
            for adj_y in range(-stroke_width, stroke_width+1):
                draw.text((x_text+adj_x, y_text+adj_y), line, font=font, fill=(0,0,0,255))
        # Interior
        draw.text((x_text, y_text), line, font=font, fill=color)
        y_text += font.size * 1.2
    return img

print("Iniciando Motor VFX Frame-por-Frame (Calidad Agencia)...")
fps = 30
duration = 2.5
total_frames = int(fps * duration)
target_w, target_h = 1080, 1920

for v_idx, video in enumerate(VIDEOS_DATA):
    print(f"-> Renderizando {video['nombre']}...")
    random.shuffle(all_images)
    selected = all_images[:3]
    clips = []
    
    for i, img_name in enumerate(selected):
        img_path = os.path.join(IMG_DIR, img_name)
        img = Image.open(img_path).convert("RGBA")
        
        width, height = img.size
        if width / height > target_w / target_h:
            new_w = int(height * (target_w / target_h))
            left = (width - new_w) / 2
            img = img.crop((left, 0, left + new_w, height))
        else:
            new_h = int(width / (target_w / target_h))
            top = (height - new_h) / 2
            img = img.crop((0, top, width, top + new_h))
            
        img = img.resize((target_w, target_h), Image.LANCZOS)
        
        # Fondo oscuro (Capa base)
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 110))
        bg_img = Image.alpha_composite(img, overlay)
        
        # Text Layer
        lines = video['textos'][i].split('\n')
        font = get_fitted_font(lines, 950, 1000, start_size=110)
        text_img = create_transparent_text(lines, target_w, target_h, font, is_cta=(i==2))
        
        # Generar Frames
        frame_pattern = os.path.join(TEMP_DIR, f"frame_{v_idx}_{i}_%03d.jpg")
        for f_idx in range(total_frames):
            frame = draw_frame(bg_img, text_img, target_w, target_h, f_idx, total_frames, clip_idx=i)
            frame.convert("RGB").save(frame_pattern % f_idx, quality=90)
            
        # Unir frames con FFmpeg
        clip_path = os.path.join(TEMP_DIR, f"clip_{v_idx}_{i}.mp4")
        cmd = [
            "ffmpeg", "-y", "-framerate", str(fps), "-i", frame_pattern,
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", clip_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clips.append(clip_path)
    
    list_path = os.path.join(TEMP_DIR, f"list_{v_idx}.txt")
    with open(list_path, "w") as f:
        for c in clips:
            f.write(f"file '{os.path.basename(c)}'\n")
            
    final_video = os.path.join(OUTPUT_DIR, f"{video['nombre']}.mp4")
    concat_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_path,
        "-c", "copy", final_video
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"   ✅ {final_video}")

shutil.rmtree(TEMP_DIR)
print("\n🎉 ¡Animaciones de Alto Nivel generadas con éxito!")
