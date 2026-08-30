from paddleocr import PaddleOCR

IMAGE = "test.jpg.jpeg"
OUTPUT = "ocr_clean.txt"

print("Starting OCR...")

ocr = PaddleOCR(lang="en")
result = ocr.predict(IMAGE)
r = result[0]

texts = r["rec_texts"]
scores = r["rec_scores"]

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("PADDLEOCR RESULTS\n")
    f.write("=" * 60 + "\n\n")

    for text, score in zip(texts, scores):
        text = text.strip()

        if not text:
            continue

        f.write(f"{score:.3f}  {text}\n")

print(f"OCR complete. Saved to: {OUTPUT}")
