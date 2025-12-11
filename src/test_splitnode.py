import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_split_delimeter(self):
       node = TextNode("This is a **text** node", TextType.TEXT)
       split_node = split_nodes_delimiter([node], "**", TextType.BOLD)

       expected = [
        TextNode("This is a ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" node", TextType.TEXT),
       ]
       self.assertEqual(split_node, expected)

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
        )
        
if __name__ == "__main__":
    unittest.main()