
from ListItemRule import ListItemRule

class ListRule(ListItemRule):

    type = 'list'
    #表示是不是在列表里面。
    inside = False
    '''
        列表是紧跟在非列表的后面，以相连的一个列表项结束
    '''
    #
    def condition(self,block):
        return True


    def action(self,block,handler):
        # 当不在列表里面 并且  内容就是列表，也就是以-开头  这个表示要开启列表的解析
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            #设置标志位：进入了列表内部
            self.inside = True
        #当 在列表里面 并且 内容不是列表条目项了  这个表示要结束列表的解析
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside = False
        return False