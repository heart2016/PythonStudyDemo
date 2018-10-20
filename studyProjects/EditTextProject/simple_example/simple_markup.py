import sys,re
from util import *
#  python simple_markup.py < ../test.txt > ../test.html   运行这个文件， 这个就是把一个 text文件转化为html带标签的文件。
#输入开始的标签字段
print('<html><head><title> </title> <body>')

title = True

# 这里就表示把  运行的时候的文件塞进来了。
for block in blocks(sys.stdin):
    #这个是正则表达式：遇到了/* */就会使用<em></em>标签替换。
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    #第一个block就会使标题
    if title:
        print('<h1>')
        #输出block
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')


