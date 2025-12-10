def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
            splitted_node = old_node.text.split(delimiter)
            for splits in splitted_node:
                new_text_node = TextNode(splits)
        raise Exception("invalid markdown syntax")