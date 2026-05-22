import os
import unittest
from dotenv import load_dotenv


class TestEnv(unittest.TestCase):
    def test_openai_api_key_loaded(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        self.assertIsNotNone(api_key, "OPENAI_API_KEY is not set in environment")
        self.assertIsInstance(api_key, str)
        self.assertTrue(api_key.startswith("sk-"), "OPENAI_API_KEY does not appear to be valid")
        self.assertGreater(len(api_key), 20, "OPENAI_API_KEY is unexpectedly short")


if __name__ == "__main__":
    unittest.main()
