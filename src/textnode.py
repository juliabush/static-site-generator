from enum inport Enum

class TextType(Enum):
    PLAIN_FORMAT = ""
    BOLD_FORMAT = "**Bold Text**"
    ITALIC_FORMAT = "_Italic Text_"
    CODE_FORMAT = "`Code text`"
    LINK_FORMAT = "[anchor text](url)"
    IMAGE_FORMAT = "![alt text](url)"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = TextType
        self.url = url 
    
    def __eq__(self, other)
    if not isinstance(other, TextNode):
        return False
    else:
        return True

    def __repr__(self)
    printNode = new TextNode()
    return f"textNode({this.text, this.text_type, this.url})"