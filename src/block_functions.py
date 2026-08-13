

def markdown_to_blocks(markdown: str) -> list[str]:
    new_blocks = []
    for block in markdown.split("\n\n"):
        if block == "":
            continue
        new_blocks.append(block.strip())
    return new_blocks
