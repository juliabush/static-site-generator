from textnode import TextType, TextNode

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