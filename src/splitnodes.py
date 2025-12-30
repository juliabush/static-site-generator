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
            continue

        text_to_process = old_node.text
        images = extract_markdown_images(text_to_process)

        if not images:
            new_nodes.append(old_node)
            continue

        current_text = text_to_process
        for alt, url in images:
            image_markdown = f"![{alt}]({url})"
            parts = current_text.split(image_markdown, 1) 

            if parts[0]: 
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            
            current_text = parts[1]
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
            
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text_to_process = old_node.text
        links = extract_markdown_links(text_to_process)

        if not links:
            new_nodes.append(old_node)

        current_text = text_to_process
        for alt, url in links:
            image_markdown = f"[{alt}]({url})"
            parts = current_text.split(image_markdown, 1) 

            if parts[0]: 
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            
            current_text = parts[1]
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
            
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes