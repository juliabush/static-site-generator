def markdown_to_blocks(markdown):
    result = []
    block_list = markdown.split("\n\n")
    for block in block_list:
        stripped_block = block.strip()
        if len(stripped_block) == 0:
            pass
        else:
            result.append(stripped_block)
    return result