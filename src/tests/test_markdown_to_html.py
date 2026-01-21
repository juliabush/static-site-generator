import unittest
from src.markdown_to_html import markdown_to_html_node
from src.htmlnode import HTMLNode, LeafNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph_conversion(self):
        markdown_input = "This is a simple paragraph."
        expected_html_node = HTMLNode(
            tag="div",
            children=[
                HTMLNode(
                    tag="p",
                    children=[
                        LeafNode(None, "This is a simple paragraph.")
                    ]
                )
            ]
        )

        result_node = markdown_to_html_node(markdown_input)

        self.assertEqual(result_node.tag, expected_html_node.tag)
        self.assertEqual(result_node.children[0].tag, expected_html_node.children[0].tag)
        self.assertEqual(result_node.children[0].children[0].value, expected_html_node.children[0].children[0].value)

