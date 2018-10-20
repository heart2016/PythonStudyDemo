
from Rule import Rule

class ListItemRule(Rule):
    type = 'listitem'

    #列表的判断条件,列表中只要以—开头的肯定是列表
    def condition(self,block):
        return block[0] == '-'

    #当时列表的
    def action(self,block,handler):
        handler.start(self.type)
        #这个表示获得字符串的。由于列表要去除—,ye就是第一个字符，所以从写了action方法。
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
