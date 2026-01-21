import unittest

from src.extract_markdown import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title_extraction(self):
        md = "This is markdown\n# Heading\n Goodbye"
        title_extraction = extract_title(md)
        self.assertEqual(
            title_extraction,
            "Heading"
        )
    
    def test_title_extraction_exception(self):
        md = "This is markdown\n Goodbye"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()