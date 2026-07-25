import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph.", {"class": "text"})
        self.assertEqual(repr(node), "LeafNode(tag=p, value=This is a paragraph., props={'class': 'text'})")

    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph.", {"class": "text"})
        self.assertEqual(node.to_html(), '<p class="text">This is a paragraph.</p>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is plain text.", None)
        self.assertEqual(node.to_html(), 'This is plain text.')

    def test_to_html_with_none_value(self):
        node = LeafNode("p", None, {"class": "text"})
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
if __name__ == "__main__":
    unittest.main()