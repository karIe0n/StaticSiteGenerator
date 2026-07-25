from textnode import TextNode, TextType

def main():
    # Example usage of TextNode
    text_node1 = TextNode("Hello, World!", TextType.PLAIN_TEXT)
    text_node2 = TextNode("This is bold text.", TextType.BOLD_TEXT)
    text_node3 = TextNode("This is italic text.", TextType.ITALIC_TEXT)
    text_node4 = TextNode("This is code text.", TextType.CODE_TEXT)
    text_node5 = TextNode("This is a link.", TextType.LINKS, url="https://example.com")
    text_node6 = TextNode("This is an image.", TextType.IMAGES, url="https://example.com/image.png")

    # Print the text nodes
    print(text_node1)
    print(text_node2)
    print(text_node3)
    print(text_node4)
    print(text_node5)
    print(text_node6)
    
if __name__ == "__main__":
    main()