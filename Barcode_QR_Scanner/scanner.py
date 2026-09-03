import cv2

IMAGE_PATH = "barcode_image.png"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print(f"Error: Could not open {IMAGE_PATH}")
else:
    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(image)

    if data:
        print("=" * 40)
        print("Type: QR CODE")
        print(f"Data: {data}")
        print("=" * 40)

        if bbox is not None:
            bbox = bbox.astype(int)

            for i in range(len(bbox[0])):
                pt1 = tuple(bbox[0][i])
                pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])
                cv2.line(image, pt1, pt2, (0, 255, 0), 2)

        cv2.imwrite("scanner_result.jpg", image)
        print("\nResult image saved as scanner_result.jpg")

    else:
        print("No QR Code detected.")
