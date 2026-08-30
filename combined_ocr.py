from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")

images = [
    "composition.jpg",
    "dose.jpg",
    "indications.jpg",
    "bottom.jpg",
]

with open("combined_ocr.txt", "w", encoding="utf-8") as f:
    for image in images:
        print(f"\n===== {image} =====")
        f.write(f"\n===== {image} =====\n")

        result = ocr.predict(image)
        r = result[0]

        for text, score in zip(r["rec_texts"], r["rec_scores"]):
            text = text.strip()

            if text:
                line = f"{score:.3f}  {text}"
                print(line)
                f.write(line + "\n")

print("\nSaved to combined_ocr.txt")