from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for index, part in enumerate(parts):
                if part == "":
                    continue
                if index % 2 == 0:
                    node = TextNode(part, TextType.TEXT)
                    new_nodes.append(node)
                else:
                    node = TextNode(part, text_type)
                    new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
           text = old_node.text
           images = extract_markdown_images(text)
           for alt, url in images:
            markdown = f"![{alt}]({url})"
            before, after = text.split(markdown, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = after
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
           text = old_node.text
           images = extract_markdown_links(text)
           for alt, url in images:
            markdown = f"[{alt}]({url})"
            before, after = text.split(markdown, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            text = after
            new_nodes.append(TextNode(after, TextType.TEXT))
    return new_nodes