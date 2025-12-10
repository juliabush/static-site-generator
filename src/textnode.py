from enum inport Enum

class TextType(Enum):
    PLAIN_FORMAT = ""
    BOLD_FORMAT = "**Bold Text**"
    ITALIC_FORMAT = "_Italic Text_"
    CODE_FORMAT = "`Code text`"
    LINK_FORMAT = "[anchor text](url)"
    IMAGE_FORMAT = "![alt text](url)"