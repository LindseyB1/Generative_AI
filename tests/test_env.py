```python
import os
import unittest
from dotenv import load_dotenv


class TestEnv(unittest.TestCase):
    def test_openai_api_key_loaded_if_present(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        if api_key is None:
            self.skipTest("OPENAI_API_KEY is not set in this environment.")

        self.assertIsInstance(api_key, str)
        self.assertTrue(
            api_key.startswith("sk-"),
            "OPENAI_API_KEY does not appear to be an OpenAI key."
        )
        self.assertGreater(
            len(api_key),
            20,
            "OPENAI_API_KEY is unexpectedly short."
        )


if __name__ == "__main__":
    unittest.main()
```
