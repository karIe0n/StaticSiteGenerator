import unittest
from src.functions import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_basic(self):
        result = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test_extract_markdown_empty(self):
        matches = extract_markdown_images("")
        self.assertListEqual([], matches)
    