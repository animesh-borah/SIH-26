from PIL import Image, ImageEnhance, ImageFilter, ImageOps

input_file = "test.jpg.jpeg"
output_file = "enhanced.jpg"

img = Image.open(input_file)

# Upscale 2x
img = img.resize(
    (img.width * 2, img.height * 2),
    Image.Resampling.LANCZOS
)

# Convert to grayscale
img = ImageOps.grayscale(img)

# Increase contrast
img = ImageEnhance.Contrast(img).enhance(1.8)

# Sharpen
img = img.filter(ImageFilter.SHARPEN)
img = img.filter(ImageFilter.SHARPEN)

# Save
img.save(output_file, quality=95)

print(f"Saved: {output_file}")
