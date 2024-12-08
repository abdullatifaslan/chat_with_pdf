import os
from services.logger import logger
import google.generativeai as genai

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self._configure()

    def _configure(self):
        genai.configure(api_key=self.api_key)

    def query(self, text: str, question: str):
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt=f"Answer the following question based on the text: {text}\nQuestion: {question}\n"

            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini API Error: {str(e)}")
            return None

