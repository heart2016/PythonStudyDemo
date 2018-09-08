#讲述学习class的python知识点

#定义类的成员变量，定义类的方法，必须要有一个self。定义self的对象的变量,否者无法设定这个对象的方法属性（也是成员变量）
class Person:
	#这个属性是私有属性。所以不能使用对象.__name访问
	_name = '私密属性'
	#这个倒是可以访问。
	userid = '110'
	def set_name(self,name):
		self.name = name;
	def get_name(self):
		return self.name;
	def greet(self):
		print(self.name);
	def set_age(self,age): #  这里一定要有self。
		self.age = age;
	#在方法的名字前面加上两个 下划线 __ （是两个下划线）这样就可以保证方法不能外部调用，是一个是有属性。
	def __printF(self,value):
		print(value)
#实例化一个对象。
person = Person();
#设定对象的值。
person.set_name('Hello')
person.greet();
# 只要设定
print(person,person.name)
print("=====================")
print(person._name)
person.set_age(10)
print(person.age)
# 这样也是可以修改对象成员变量的值。也可以调用set_age。
person.age = 20
print(person.age)
#报错，不能访问那个方法啊
#person.__printF(10.0);
#这样会报错的，只能通过方法修改的
#print(person.__name) # 这个方法会报错
print(person.userid)