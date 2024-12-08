import unittest
from services.gemini_service import GeminiService

class TestGeminiService(unittest.TestCase):
    def setUp(self):
        self.gemini_service = GeminiService()

    def test_query(self):
        context = """
                Artificial Intelligence (AI) refers to the simulation of human intelligence in machines programmed to think, learn, and solve problems. AI systems can perform tasks that typically require human cognition, such as decision-making, natural language processing, visual perception, and speech recognition.

                AI is categorized into:

                Narrow AI: Narrowly focused on one task, such as a virtual assistant capable of understanding voice commands, like Siri or Alexa. General AI: Imaginary AI that can execute any intellectual task which can be done by a human being.
                Key techniques include machine learning, where systems learn patterns from data, and deep learning-a subset of ML using neural networks. AI is used in a variety of fields, including healthcare, finance, robotics, and entertainment.

                With immense potential comes artificial intelligence, bringing ethical issues including job displacement, privacy, and transparency of decision-making.
        """
        question = "What is this document about?"
        answer = self.gemini_service.query(context, question)
        self.assertIsNotNone(answer)
        self.assertIsInstance(answer, str)

if __name__ == "__main__":
    unittest.main()
