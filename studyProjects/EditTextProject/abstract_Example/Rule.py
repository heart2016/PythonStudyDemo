# 书写规则的超累
# 这个类的作用就是规定解析规则，在这里调用解析类Handler。并且每个子类都必须有一个属性type。
# 每一个规则都必须有两个方法：condition 条件  和  action 操作
class Rule:
    #所有排版当时的积累方法
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        # 这里调用诸如handler.start('headline') hand.feed()
        # 当规则调用完了返回True
        return True