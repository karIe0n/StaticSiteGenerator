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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is a bold text node")
    
    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "This is an italic text node")
        
    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
    
    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "http://example.com")
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "http://example.com"})
    
    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "http://example.com/image.png")
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "This is an image text node"})
    

if __name__ == "__main__":
    unittest.main()