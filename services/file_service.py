import uuid
import re
import os
from PyPDF2 import PdfReader
from services.logger import logger

class FileService:
    def __init__(self):
        self.data_store = {}

    def save_file(self, file):
        try:
            file_id = self.document_id()
            file_path = f"storage/{file_id}.pdf"
            with open(file_path, "wb") as saved_file:
                saved_file.write(file)
            logger.info(f"File saved: {file_path}")


            reader = PdfReader(file_path)
            text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
            extracted_text = self.process_text(text)
            logger.info(f"Text extracted from {file_path}")

            self.data_store[file_id] = {
                "filename": os.path.basename(file_path),
                "page_count": len(reader.pages),
                "text": extracted_text,
            }
            logger.info(f"PDF {file_path} loaded successfully with ID {file_id}.")
            
            return file_id, file_path
        except Exception as e:
            logger.error(f"Error saving file: {str(e)}")
            raise
    
    @staticmethod
    def document_id():
        return str(uuid.uuid4())
    
    @staticmethod
    def process_text(text):
        text = re.sub(r'\s+', ' ', text)  
        text = text.strip()
        return text
    
