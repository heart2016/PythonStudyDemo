#一个工具类

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

def lines(file):
    for line in file: yield line
    yield '\n'