#  解析类，也是核心类
import re
from util import *
class Parse:
    def __init__(self,handler):
        #初始化操作类
        self.handler = handler
        #初始化规则，可能有很多规则
        self.rules = []
        #初始化过滤器,筛选出符合正则表达式的字符串片段
        self.filters = []
    #添加排版规则。
    def addRule(self,rule):
        self.rules.append(rule)
    #添加正则表达式的筛选Pattern
    def addFilter(self,pattern,name):
        #定义一个过滤器的方法。这个也其实就是正则表达式的方法。表示筛选出符合正则的字符串片段
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    #表示开始解析文件
    def parse(self,file):

        #开始文本处理
        self.handler.start('document')
        #读取文件的所有数据
        #从文本总获得的每一个 block 也就是段落，都需要经历：过滤，排版规则的操作
        for block in blocks(file):
            # 迭代选出该block属于那种排版规则
            for rule in self.rules:

                if rule.condition(block):

                    # 如果当前的block属于这个排版规则，那么就需要处理，获得新的字符串last，已经在里面替换了
                    last = rule.action(block, self.handler)
                    # 这个last表示排版结束，那么这个block可以结束迭代排版。
                    # 判断是不是属于当前的排版rule规则
                    # 迭代所有过滤规则，也就是正则规则  选出属于何种
                    for filter in self.filters:
                        # print('block=', block)
                        # 使用规则替换
                        block = filter(block, self.handler)
                    if last: break



            #结束文本处理
        self.handler.end('document')

