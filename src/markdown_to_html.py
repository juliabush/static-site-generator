from markdown_to_block import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from splitnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level = level +1
                else:
                    break
            text = block[level:].lstrip()
            children = text_to_children(text)
            tag = f"h{level}"
            result = ParentNode(tag, children=children)
            block_nodes.append(result)


        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            result = ParentNode("p", children=children)
            block_nodes.append(result)


        if block_type == BlockType.CODE:
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            code_text = "\n".join(inner_lines)
            code_node = LeafNode("code", value=code_text)
            pre_node = ParentNode("pre", children=[code_node])
            block_nodes.append(pre_node)


        if block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            number = 1
            for line in lines:
                parts = line.split(". ", 1)
                if len(parts) == 2:
                    cleaned_line = parts[1]
                else:
                    cleaned_line = line 
                children = text_to_children(cleaned_line)
                li_node = ParentNode("li", children=children)
                li_nodes.append(li_node)
            result = ParentNode("ol", children=li_nodes)
            block_nodes.append(result)


        if block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                if line.startswith("- "):
                    cleaned_line = line[2:]
                else:
                    cleaned_line = line
                children = text_to_children(cleaned_line)
                li_node = ParentNode("li", children=children)
                li_nodes.append(li_node)
            result = ParentNode("ul", children=li_nodes)
            block_nodes.append(result)
        
        if block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                cleaned_line = line.lstrip("> ").strip()
                cleaned_lines.append(cleaned_line)
            children = text_to_children(" ".join(cleaned_lines))
            result = ParentNode("blockquote", children=children)
            block_nodes.append(result)
    
    return ParentNode("div", children=block_nodes)

def text_to_children(text):
    children = []
    text_node = text_to_textnodes(text)
    print(f"text_to_textnodes returned: {text_node}")
    for tn in text_node:
        child = text_node_to_html_node(tn)
        children.append(child)
    return children