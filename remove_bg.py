from PIL import Image
import numpy as np

img = Image.open("core/static/logo.png").convert("RGBA")
data = np.array(img)

r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Make dark/near-black pixels transparent (background removal)
# Pixels that are dark (all channels < 40) or near-dark navy (#0f172a, #1e1e2f)
is_dark = (r < 60) & (g < 60) & (b < 80)

# Also remove navy blue backgrounds (#0f172a range)
is_navy = (r < 50) & (g < 40) & (b < 60)

# Combined mask
mask = is_dark | is_navy

# Set alpha to 0 for background pixels
data[:,:,3][mask] = 0

# For near-background pixels, semi-transparent
near_mask = (r < 80) & (g < 70) & (b < 100) & ~mask
data[:,:,3][near_mask] = (data[:,:,3][near_mask] * 0.3).astype(np.uint8)

result = Image.fromarray(data)
result.save("core/static/logo.png", "PNG")
print("Logo background removed and saved!")
