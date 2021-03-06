#类的方法重写：包括普通方法和构造方法

#1、重写父类的普通方法

class A:
	def __init__(self,value = 45):
		print('A的构造方法')
		self.value = value
	def show(self):  #注意对象的方法，一定要有参数self  表示可以被对象调用,对象方法可以：对象.方法名（参数）这样调用，还可以这样：类名.(对象，参数)也是合法的
		print('我是A=======>')
	def hello(self):
		print('Hello====A',self.value)
	def __h__(self):  #这个有self，表示只能使用对象调用。
		print('HHHHHH')
	def __j__():  #这个也是直接使用类名调用
		print('JJJJJJJ')
		
	def x():#没有self  就表示是静态方法，可以使用类名直接调用。
		print('XXXX')
		
		
#子类B		
class B(A):
	def __init__(self): #但是构造方法就比较特殊，可以使用类名调用
		#A.__init__(self) # 这样就是调用了父类的构造方法
		super().__init__()#这样也是调用了父类构造方法
		print('B的构造方法')
	def show(self): #注意对象的方法，一定要有参数self  表示可以被对象调用。  这里没有self  也会报错，就算是重写父类的方法
		print('我是B========')  #这样就是把父类的方法覆写了，这样只会执行子类的代码块啦

a = A()
b = B()

a.show()
b.show() #只会执行：我是B====
a.hello()  #这行代码打印的是：Hello====A

b.hello()  #这行代码会报错，这是因为在初始化的时候，没有调用父类的构造函数。 如果B的构造方法中调用了：A.__init__(self)  就不会报错了


print('===参数===>',a.value)  #  这个可以打印出45

A.hello(a) #这样就是：类名.方法（对象,参数）这样也是合法的调用   所以这里不会报错
a.__h__();
A.__h__(a)
A.__j__()
A.x()