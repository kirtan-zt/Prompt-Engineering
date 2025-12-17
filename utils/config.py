import os
import time
from dotenv import load_dotenv
from google import genai
from loguru import logger

# Load environment variables once when this module is imported
load_dotenv()

def get_gemini_client():
    """
    Initializes and returns the Gemini client.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY is missing from environment variables.")
        raise ValueError("GEMINI_API_KEY not found.")
    
    return genai.Client(api_key=api_key)

# Define constants here so they are consistent across your project
DEFAULT_MODEL = 'gemini-2.5-flash-lite'

def handle_api_error(e, attempt):
    """
    Global error handler for common Gemini API issues.
    Returns the wait time if retryable, otherwise raises the error.
    """
    error_msg = str(e)
    if "429" in error_msg or "503" in error_msg:
        wait_time = (attempt + 1) * 30 
        logger.warning(f"Rate limit/Service error. Attempt {attempt + 1}. Waiting {wait_time}s...")
        time.sleep(wait_time)
        return True
    return False