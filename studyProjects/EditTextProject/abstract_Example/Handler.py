#处理程序的超类

class Handler:
    #指定回调接口，后面的方法都会通过这个放来来调用
    #参数：prefix 方法名的前缀   name：方法名   # *args:可变参数。
    def callback(self,prefix,name,*args):
        #有点类似反射，获得方法对象
        method = getattr(self,prefix + name,None)
        #判断方法是不是可以调用。可以被调用就调用该方法。
        if callable(method): return method(*args)
    #辅助方法：这个的意思就是使用：start前缀，后面就是name
    def start(self,name):
        self.callback('start_', name)
    #辅助方法：这个意思是使用end_  后面是name。
    def end(self,name):
        self.callback('end_',name)
    #辅助方法：前面是sub   后面是name。  这个方法的返回值是  一个函数：substitution
    def sub(self,name):
        # match：这个就是前面的使用正则表达式匹配了之后的生成的字符串
        def substitution(match):
            # print('===',match)
            # 这里返回的就是置换了之后的结果。也就是<em> </em>
            result = self.callback('sub_',name,match)
            if result is None: match.group(0)
            return result
        return substitution