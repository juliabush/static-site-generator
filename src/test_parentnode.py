import unittest

from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")




if __name__ == "__main__":
    unittest.main()