import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split(self):
       node = TextNode("This is a **text** node", TextType.TEXT)
       split_node = split_nodes_delimiter([node], "**", TextType.BOLD)

       expected = [
        TextNode("This is a ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" node", TextType.TEXT),
       ]
       self.assertEqual(split_node, expected)

if __name__ == "__main__":
    unittest.main()