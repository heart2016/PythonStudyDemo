
# 解析标题的规则  标题的排版规则。
from Rule import *
class HeadingRule(Rule):
    type = 'heading'
    #判断字符串block是不是符合当前要排版的要求,也就是判断传入的字符串是不是要使用当前的排版规则
    def condition(self,block):
        # 如果文本块符合标题定义，就返回True，否者返回False。
        #这表示标题是：没有换行符  并且  长度小于70 并且  最后一个字符不能以:冒号结尾。
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'