from enum import Enum

export class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

export class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url 
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        else:
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
               return True

    def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"