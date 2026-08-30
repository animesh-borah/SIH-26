from paddleocr import PaddleOCR

IMAGE = "test.jpg.jpeg"
OUTPUT = "ocr_high_confidence.txt"

print("Starting OCR...")

ocr = PaddleOCR(lang="en")
result = ocr.predict(IMAGE)
r = result[0]

texts = r["rec_texts"]
scores = r["rec_scores"]

with open(OUTPUT, "w", encoding="utf-8") as f:
    for text, score in zip(texts, scores):
        text = text.strip()

        if text and score >= 0.80:
            f.write(f"{score:.3f}  {text}\n")

print(f"Saved high-confidence OCR to: {OUTPUT}")
