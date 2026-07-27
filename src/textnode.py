from enum import Enum
from src.leafnode import LeafNode


class TextType(Enum):
    TEXT = "plain text"
    BOLD = "**bold text**"
    ITALIC = "_italic text_"
    CODE = "`code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](image url)"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self, text_node: TextNode) -> LeafNode:
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("strong", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("em", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            if not text_node.url:
                raise Exception("URL is required for link text type")
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            if not text_node.url:
                raise Exception("URL is required for image text type")
            return LeafNode("img", None, props={"src": text_node.url, "alt": text_node.text})
        else:
            raise Exception(f"Unsupported text type: {text_node.text_type}")
