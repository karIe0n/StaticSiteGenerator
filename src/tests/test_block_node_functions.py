import unittest
from src.blocknode import BlockType, BlockNode

class TestBlockNodeFunctions(unittest.TestCase):
    
    def test_heading(self):
        block = "### Heading 1"
        self.assertEqual(BlockType.HEADING, BlockNode.block_to_block_type(block))
        
    def test_code(self):
        block = """
        ```
        a = 1
        b = 2
        if a != b:
            return a + b
        else:
            return a - b
        ```
        """
        self.assertEqual(BlockType.CODE, BlockNode.block_to_block_type(block))
        
    def test_quote(self):
        block = """
        > this is my planet!
        >no
        """
        self.assertEqual(BlockType.QUOTE, BlockNode.block_to_block_type(block))
        
    def test_unordered_list(self):
        block = """
        - banana
        -orange
        - cucumber
        """
        self.assertEqual(BlockType.UNORDERED_LIST, BlockNode.block_to_block_type(block))
        
    def test_ordered_list(self):
        block = """
        1. jamie
        2. susan
        3. peter
        """
        self.assertEqual(BlockType.ORDERED_LIST, BlockNode.block_to_block_type(block))
    
    def test_ordered_list_no_whitespace_after_counter(self):
        block = """
        1.jamie
        2.susan
        3.peter
        """
        self.assertEqual(BlockType.PARAGRAPH, BlockNode.block_to_block_type(block))
        
    