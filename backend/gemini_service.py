import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_chat_response(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(os.getenv("MODEL_NAME", "gemini-1.5-flash-latest"))
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Sorry, I encountered an error."