def markdown_to_blocks(markdown):
    block_list = []
    block = markdown.split("\n\n")
    stripped_block = block.strip()
    if len(stripped_block) == 0:
        pass
    else:
        block_list.append(block)
    return block_list