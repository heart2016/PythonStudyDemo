
import re
from HTMLRender import *
handler = HTMLRender()
#  handler.sub('emphasis')  这个会有一个参数是  正则表达式匹配出的字符串会传入，该函数中。也就是 * is *
result = re.sub(r'\*(.+?)\*',handler.sub('emphasis'),'This *is* a test')
print(result)