#类的第三个例子文件
class C:
	#只要是初始化的时候都会调用这种语句。也就是裸代码。有点类似静态代码，一旦载入，就会执行的代码
	#这就类似于静态代码块。
	print('类的字节码文件');
	#这样就有点类似于静态变量啦  
	member = 0
	
	def init(self):
		print('初始化');
	def set_name(self,name):
		self.name = name
	def get_name(self):
		return self.name;

#c = C()
#c.init()
c1 = C()
C.member += 10
print(C.member);
print(c1.member)

class A(C):
	print('A 类')
	
print("子类父类",issubclass(A,C)) #True  
print("子类父类",issubclass(C,C)) #True
print("子类父类",issubclass(C,A)) #False
a = A()
print(isinstance(c1,C)) #True
print(isinstance(a,C))	#True

print('属性是否可以调用',callable(getattr(a,'name','是否'))) #False
a.set_name('傻逼')
print('属性是否可以调用',callable(getattr(a,'name','是否'))) #False
print('属性是否可以调用',callable(getattr(a,'member','是否'))) #False
# 说明这个只是检测方法可以不可以调用的。中间参数一定是方法名。也就是说  可以通过方法hasattr(对象，'方法名') 来检测对象是不是存在方法。
print('属性是否可以调用',callable(getattr(a,'init','是否'))) #True