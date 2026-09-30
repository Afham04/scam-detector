import io

import pytesseract
from PIL import Image, ImageEnhance

from config import Config

if Config.TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD


def extract_text_from_image(image_bytes: bytes) -> dict:
    if not image_bytes:
        return {"success": False, "error": "No image data provided", "extracted_text": ""}

    try:
        image = Image.open(io.BytesIO(image_bytes))

        if image.mode in ("P", "RGBA"):
            image = image.convert("RGB")

        gray_image = image.convert("L")
        enhanced_image = ImageEnhance.Contrast(gray_image).enhance(1.8)

        extracted_text = pytesseract.image_to_string(enhanced_image)
        cleaned_text = extracted_text.strip()

        if not cleaned_text:
            extracted_text = pytesseract.image_to_string(image)
            cleaned_text = extracted_text.strip()

        return {
            "success": True,
            "extracted_text": cleaned_text,
            "character_count": len(cleaned_text),
            "message": "Text extracted successfully" if cleaned_text else "No text detected in image"
        }
    except Exception as exc:
        return {
            "success": False,
            "error": f"Failed to process image: {str(exc)}",
            "extracted_text": ""
        }
