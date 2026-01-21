import unittest
import os
import tempfile

from generate import generate_page

class TestGeneratePage(unittest.TestCase):
    def test_generate_page_creates_html(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            md_path = os.path.join(temp_dir, "test.md")
            template_path = os.path.join(temp_dir, "template.html")
            dest_path = os.path.join(temp_dir, "out.html")

            with open(md_path, "w") as f:
                f.write("# Hello\n\nThis is **bold** text.")

            with open(template_path, "w") as f:
                f.write("<html><head><title>{{ Title }}</title></head>"
                        "<body>{{ Content }}</body></html>")

            generate_page(md_path, template_path, dest_path, "/")

            self.assertTrue(os.path.exists(dest_path))

            with open(dest_path, "r") as f:
                output = f.read()

            self.assertIn("<h1>Hello</h1>", output)
            self.assertIn("<b>bold</b>", output)
            self.assertIn("<title>Hello</title>", output)


if __name__ == "__main__":
    unittest.main()
