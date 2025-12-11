import unittest

from splitnodes import split_nodes_delimeter

def test_split(self):
       node = TextNode("This is a **text** node", TextType.BOLD)
       split_node = split_nodes_delimiter(node, "**", TextType.BOLD)
       self.assertEqual(split_node, node)

if __name__ == "__main__":
    unittest.main()