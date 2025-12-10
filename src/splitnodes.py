def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_list = []
    for old_node in old_nodes:
        if old_node is not TextType.TEXT:
            new_list.append(old_node)
            raise Exception("invalid markdown syntax")