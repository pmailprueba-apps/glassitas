from PIL import Image, ImageOps
import os

base_img_path = 'assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/0047ac48-1662-4bcc-88b1-e547cdc92e8e.jpg'
frame_path = 'assets/logo/escaletas/escaleta horizontal 2.png'

base_img = Image.open(base_img_path).convert("RGBA")
frame = Image.open(frame_path).convert("RGBA")

# Resize base_img to cover the frame (ImageOps.fit does this by cropping the center)
# But we can also scale it manually. Let's use fit since the user's images have white borders
fitted_base = ImageOps.fit(base_img, frame.size, method=Image.Resampling.LANCZOS)

# Paste frame on top
final = Image.alpha_composite(fitted_base, frame)

# Convert to RGB and save
final.convert("RGB").save("test_output.jpg")
print("Saved test_output.jpg")
