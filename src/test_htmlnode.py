import unittest
import htmlnode as HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode.HTMLNode("div", "Hello, World!", {"class": "greeting"}, [])
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, props={'class': 'greeting'}, children=[])")

    def test_props_to_html(self):
        node = HTMLNode.HTMLNode("div", None, {"class": "greeting", "id": "main"}, [])
        self.assertEqual(node.props_to_html(), ' class="greeting" id="main"')

    def test_props_to_html_empty(self):
        node = HTMLNode.HTMLNode("div", None, {}, [])
        self.assertEqual(node.props_to_html(), '')
    
    def test_props_to_html_none(self):
        node = HTMLNode.HTMLNode("div", None, None, [])
        self.assertEqual(node.props_to_html(), '')
    
    def test_to_html_not_implemented(self):
        node = HTMLNode.HTMLNode("div", "Hello, World!", {"class": "greeting"}, [])
        with self.assertRaises(NotImplementedError):
            node.to_html()
            
    def test_children_default(self):
        node = HTMLNode.HTMLNode("div", "Hello, World!", {"class": "greeting"}, None)
        self.assertEqual(node.children, [])
    
    def test_node_with_children(self):
        child_node = HTMLNode.HTMLNode("span", "Child", {"class": "child"}, [])
        node = HTMLNode.HTMLNode("div", "Hello, World!", {"class": "greeting"}, [child_node])
        self.assertEqual(node.children, [child_node])


if __name__ == "__main__":
    unittest.main()