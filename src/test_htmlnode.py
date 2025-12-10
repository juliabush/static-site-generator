import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_all_default(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_eq(self):
        node = HTMLNode("h1", "hello world", )
        node2 = HTMLNode("h1", "hello world", )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("h1", "I love dogs", )
        node2 = HTMLNode("p", "Cats are the best", )
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()