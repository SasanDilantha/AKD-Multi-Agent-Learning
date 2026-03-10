from dotenv import load_dotenv
import os

load_dotenv()

def mask_api_key(key: str) -> str:
    if len(key) <= 8:
        return "****"
    return key[:4] + "****" + key[-4:]

def get_google_api_key() -> str:
    google_api_key = os.environ.get("MODEL_API_KEY", "")
    if not google_api_key:
        raise ValueError("MODEL_API_KEY environment variable not set.")
    return google_api_key

def get_model_name() -> str:
    model_name = os.environ.get("MODEL_NAME", "")
    if not model_name:
        raise ValueError("MODEL_NAME environment variable not set.")
    return model_name
