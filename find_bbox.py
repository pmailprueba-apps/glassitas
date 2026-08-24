from PIL import Image
import numpy as np

frame_path = 'assets/logo/escaletas/escaleta horizontal 2.png'
frame = Image.open(frame_path).convert("RGBA")
arr = np.array(frame)

# Alpha channel
alpha = arr[:, :, 3]

# Find where alpha is 0 (transparent)
y_indices, x_indices = np.where(alpha == 0)

if len(y_indices) > 0:
    x_min, x_max = x_indices.min(), x_indices.max()
    y_min, y_max = y_indices.min(), y_indices.max()
    print(f"Transparent window bounding box: x=({x_min}, {x_max}), y=({y_min}, {y_max})")
    print(f"Window size: {x_max - x_min}x{y_max - y_min}")
else:
    print("No fully transparent pixels found.")

# Let's also check for partially transparent
y_indices, x_indices = np.where(alpha < 255)
if len(y_indices) > 0:
    x_min, x_max = x_indices.min(), x_indices.max()
    y_min, y_max = y_indices.min(), y_indices.max()
    print(f"Partial transparency bounding box: x=({x_min}, {x_max}), y=({y_min}, {y_max})")
    print(f"Window size: {x_max - x_min}x{y_max - y_min}")
