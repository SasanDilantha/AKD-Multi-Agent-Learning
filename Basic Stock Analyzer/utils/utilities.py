
import os
from dotenv import load_dotenv

load_dotenv()

def mask_api_key(key: str) -> str:
    if len(key) <= 8:
        return "****"
    return key[:4] + "****" + key[-4:]

def get_google_api_key() -> str:
    google_spi_key = os.environ.get("GOOGLE_API_KEY", "")
    if not google_spi_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    return google_spi_key