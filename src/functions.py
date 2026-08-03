from src.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if delimiter not in old_node.text:
            raise Exception("delimiter is not found in the text node")
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text) -> list[tuple]:
    matches = re.findall(r"!\[[\w ]+\]\(https:[/\w\d.]+\)", text)
    result = []
    for match in matches:
        split = match.split("(")
        new_tuple = (split[0].strip("![]"), split[1].strip(")"))
        result.append(new_tuple)
    return result

def extract_markdown_links(text) -> list[tuple]:
    matches = re.findall(r"\[[\w ]+\]\(https[\w:/.@]+\)", text)
    result = []
    for match in matches:
        split = match.split("(")
        new_tuple = (split[0].strip("[]"), split[1].strip(")"))
        result.append(new_tuple)
    return result

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    
    
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]: