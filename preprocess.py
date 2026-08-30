import cv2

input_file = "test.jpg.jpeg"
output_file = "processed.jpg"

img = cv2.imread(input_file)

if img is None:
    raise FileNotFoundError(f"Could not read {input_file}")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Improve contrast
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)
enhanced = clahe.apply(gray)

# Reduce noise
denoised = cv2.fastNlMeansDenoising(
    enhanced,
    None,
    10,
    7,
    21
)

# Adaptive threshold
processed = cv2.adaptiveThreshold(
    denoised,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31,
    11
)

cv2.imwrite(output_file, processed)

print(f"Saved: {output_file}")