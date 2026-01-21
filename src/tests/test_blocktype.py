import unittest

from src.blocktype import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# My heading"
        assert block_to_block_type(block) == BlockType.HEADING

        block2 = "- Hello\n- Bye\n- Goodnight"
        assert block_to_block_type(block2) == BlockType.UNORDERED_LIST

        block3 = "manchild, why you always come runnin to me"
        assert block_to_block_type(block3) == BlockType.PARAGRAPH

        block4 = "1. Hello\n2. Goodbye"
        assert block_to_block_type(block4) == BlockType.ORDERED_LIST
