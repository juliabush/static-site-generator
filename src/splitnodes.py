def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimeter)
            if len(parts) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for index, part in enumerate(parts):
                if index % 2 == 0:
                    node = TextNode(part, TextType.TEXT)
                else:
                    node = TextNode(part, text_type)
                
                new_nodes.append(node)