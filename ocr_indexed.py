from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")

image = "test.jpg.jpeg"
output = "ocr_indexed.txt"

result = ocr.predict(image)
r = result[0]

texts = r["rec_texts"]
scores = r["rec_scores"]

with open(output, "w", encoding="utf-8") as f:
    for i, (text, score) in enumerate(zip(texts, scores)):
        text = text.strip()

        if text:
            line = f"{i:02d}  {score:.3f}  {text}"
            print(line)
            f.write(line + "\n")

print()
print(f"Saved to: {output}")
