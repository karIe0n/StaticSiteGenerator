import unittest
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, **bold text**, None)")
        
    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "http://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, [anchor text](url), http://example.com)")
    
    def test_repr_with_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "http://example.com/image.png")
        self.assertEqual(repr(node), "TextNode(This is a text node, ![alt text](image url), http://example.com/image.png)")
        
    def test_repr_with_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(repr(node), "TextNode(This is a text node, `code text`, None)")


if __name__ == "__main__":
    unittest.main()