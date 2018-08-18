#第九章的小知识点  构造函数讲解

#在python3中。都是新式类。所以不需要显示的继承object

#初讲 构造函数  

#构造函数几点：名字一定是__init__  注意前后是双下滑下，也就是两个下划线。 前后加起来四个下划线。名字一定是init。
class One:
	def __init__(self,value=42):
		self.firstValue = value;
		print('初始化构造函数')
#one = One();
#print('====>',one.firstValue)

#析构函数，在销毁之前调用 名字是__del__

class Two:
	def __init__(self):
		print('初始化构造函数')
	def __del__(self):
		print('调用了析构函数')
two = Two();
