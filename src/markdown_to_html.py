from markdown_to_block import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode
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
            result = HTMLNode(tag, children=children)
            block_nodes.append(result)


        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            result = HTMLNode("p", children=children)
            block_nodes.append(result)


        if block_type == BlockType.CODE:
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            code_text = "\n".join(inner_lines)
            code_node = HTMLNode("code", value=code_text)
            pre_node = HTMLNode("pre", children=[code_node])
            block_nodes.append(pre_node)


        if block_type == BlockType.ORDERED_LIST:
            children = text_to_children(block)
            result = HTMLNode("ol", children=children)
            block_nodes.append(result)


        if block_type == BlockType.UNORDERED_LIST:
            children = text_to_children(block)
            result = HTMLNode("ul", children=children)
            block_nodes.append(result)
        
        if block_type == BlockType.QUOTE:
            children = text_to_children(block)
            result = HTMLNode("blockquote", children=children)
            block_nodes.append(result)
    
    return HTMLNode("div", children=block_nodes)

def text_to_children(text):
    children = []
    text_node = text_to_textnodes(text)
    print(f"text_to_textnodes returned: {text_node}")
    for tn in text_node:
        child = text_node_to_html_node(tn)
        children.append(child)
    return children