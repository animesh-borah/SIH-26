import cv2

images = [
    "..\image1.jpeg",
    "..\image2.jpeg",
    "..\image3.jpeg",
    "..\image4.jpeg",
    "..\image5.jpeg"
]

detector = cv2.barcode.BarcodeDetector()

print("=" * 55)
print("BARCODE SCANNER RESULTS")
print("=" * 55)

for image_path in images:
    image = cv2.imread(image_path)

    if image is None:
        print(f"\nERROR: Could not open {image_path}")
        continue

    decoded_data, bbox, _ = detector.detectAndDecode(image)

    print(f"\nImage: {image_path}")

    if decoded_data:
        print("Status: SUCCESS")
        print(f"Barcode Data: {decoded_data}")

    elif bbox is not None:
        print("Status: BARCODE DETECTED BUT NOT DECODED")

    else:
        print("Status: NO BARCODE DETECTED")

print("\n" + "=" * 55)
print("SCAN COMPLETE")
print("=" * 55)
