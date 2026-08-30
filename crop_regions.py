from PIL import Image

img = Image.open("test.jpg.jpeg")

print("Image size:", img.size)

# Original image is 900 x 1600
# Crop regions for separate OCR processing

crops = {
    "top.jpg": (0, 0, 900, 260),
    "composition.jpg": (0, 180, 900, 550),
    "dose.jpg": (0, 500, 900, 900),
    "indications.jpg": (0, 820, 900, 1200),
    "bottom.jpg": (0, 1150, 900, 1600),
}

for filename, box in crops.items():
    crop = img.crop(box)

    # 2x upscale
    crop = crop.resize(
        (crop.width * 2, crop.height * 2),
        Image.Resampling.LANCZOS
    )

    crop.save(filename, quality=95)
    print("Saved:", filename)

