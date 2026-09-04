from barcode_scanner import scan_barcode_from_file

image_path = r"..\image1.jpeg"

result = scan_barcode_from_file(image_path)

print("\nBARCODE SCAN RESULT")
print("=" * 50)

for key, value in result.items():
    print(f"{key}: {value}")