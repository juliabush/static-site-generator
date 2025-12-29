from enum import Enum



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

# example of type hinting 
def block_to_block_type(block:str) -> BlockType:
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith("#") and " " in block:
        return BlockType.HEADING
    
    lines = block.split("\n")

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                break
        else:
            return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                break
        else:
            return BlockType.UNORDERED_LIST
        
    number = 1
    if block.startswith(f"{number}. "):
        for line in lines:
            if not line.startswith(f"{number}. "):
                break
            number = number + 1
        else:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH