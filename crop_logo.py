from PIL import Image
import numpy as np

img = Image.open("core/static/logo.png").convert("RGBA")
w, h = img.size
print(f"Original size: {w} x {h}")

# Crop top 75% of the image (removes the text at the bottom)
crop_h = int(h * 0.72)
cropped = img.crop((0, 0, w, crop_h))

# Also trim whitespace/transparent edges using numpy
data = np.array(cropped)
alpha = data[:,:,3]

# Find rows and cols with non-transparent pixels
rows = np.any(alpha > 10, axis=1)
cols = np.any(alpha > 10, axis=0)

if rows.any() and cols.any():
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    # Add a small padding
    pad = 10
    rmin = max(0, rmin - pad)
    rmax = min(crop_h - 1, rmax + pad)
    cmin = max(0, cmin - pad)
    cmax = min(w - 1, cmax + pad)
    cropped = cropped.crop((cmin, rmin, cmax + 1, rmax + 1))

print(f"Cropped size: {cropped.size}")
cropped.save("core/static/logo.png", "PNG")
print("Done! Logo cropped to icon-only.")
