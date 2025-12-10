from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node not in TextType:
        raise Exception
    else:
        if text_node.text_type == TextType.TEXT:
            return LeafNode(value)
        if text_node.text_type == TextType.BOLD:
            return LeafNode("<b>", value)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode("<i>", value)
        if text_node.text_type == TextType.CODE:
            return LeafNode("<code>", value)
        if text_node.text_type == TextType.LINK:
            return LeafNode("<a>", value, "href")
        if text_node == TextType.IMAGE:
            return LeafNode("<img>", "", "src", "alt")
