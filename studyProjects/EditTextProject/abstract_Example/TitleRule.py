
# 解析标题的规则  标题的排版规则。
from Rule import *
from HeadingRule import HeadingRule
class TitleRule(Rule):
    type = 'title'
    first = True
    #判断是不是标题
    def condition(self,block):
        # 上面的标题一顶要是True
        if not self.first: return False
        #之后再修改为Flase
        self.first = False
        #并且判断是不是标题
        return HeadingRule.condition(self,block)