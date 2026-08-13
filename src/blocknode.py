from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

class BlockNode:
    def block_to_block_type(block: str) -> BlockType:
        if re.search(r'#{1,6}\s(.*?)+', block) != None:
            return BlockType.HEADING
        elif re.search(r'```\n[\w\s:!=()+-/]+```', block) != None:
            return BlockType.CODE
        elif re.search(r'>\s?[\w\n]+', block) != None:
            return BlockType.QUOTE
        elif re.search(r'-\s[\w]+', block) != None:
            return BlockType.UNORDERED_LIST
        elif BlockNode.is_ordered_list(block):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    
    def is_ordered_list(block: str) -> bool:
        counter = 1
        is_ordered = False
        blocks = block.split("\n")
        for block in blocks:
            block = block.strip()
            if block == "":
                continue
            if f"{counter}. " not in block:
                return is_ordered
            else:
                counter += 1
                is_ordered = True
        return is_ordered
        