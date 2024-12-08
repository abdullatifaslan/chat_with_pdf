import unittest
import os
from PyPDF2 import PdfWriter

from tempfile import TemporaryDirectory
from services.file_service import FileService

class TestFileService(unittest.TestCase): 
    def setUp(self):
        self.pdf_path = 'sample.pdf'
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)
        with open(self.pdf_path, "wb") as f:
            writer.write(f)

    
    def test_pdf_file_reading(self):
        try:
            with open(self.pdf_path, "rb") as pdf_file:
                file_service = FileService()
                self.file_id , self.file_path = file_service.save_file(pdf_file.read())
            
            self.assertIn('storage',self.file_path)
        except Exception as e:
            self.fail(f"Failed to read PDF file: {e}")


    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            os.remove(self.pdf_path)

if __name__ == "__main__":
    unittest.main()
