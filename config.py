import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-scam-detector-2025")
    AI_API_KEY = os.getenv("AI_API_KEY", "")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")
    AI_API_URL = os.getenv("AI_API_URL", "")
    TESSERACT_CMD = os.getenv("TESSERACT_CMD")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
