def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
                 # 1. split the text
        # 2. check for valid delimiter pairs
        # 3. build new TextNodes and append to new_nodes
            splitted_node = old_node.text.split(delimiter)
            for index, part in enumerate(splitted_node):
                new_text_node = TextNode(splits)
        raise Exception("invalid markdown syntax")