# 一个工具类，用于读取文件和文本的
# 加载文件中的所有文本信息, 注意这里的yield非常重要，一个函数里面有了yield，那么这个的返回值就会是一个迭代器，就可以当作list使用。
#所以这个方法的返回值，是整个file里面的所有行。
def loadLines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in file:
        # strip去除前后的空格键  line.strip() 去除字符串前后的空格
        if line.strip():
            block.append(line)
        # 当line去掉空格是为空，那么就判断block是不是空
        elif block:
            #这个就是把block里面的所有line都用'' 连接起来。
            yield ''.join(block).strip()
            block = []



