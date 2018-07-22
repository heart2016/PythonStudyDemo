#说明抽象方法的定义方式
from abc import ABC, abstractmethod
class Talker(ABC):  #  有了注解，并且还要集成ABC 这个类，否者也不是抽象类，否者也是可以实例化的。也就是说
	@abstractmethod #只要方法加了这个注解，就表示该方法是抽象方法
	def talk(self):
		pass;
#也就是说：继承ABC 并且有方法加了注解@abstractmethod才能是抽象方法
		
#talk = Talker()  #实例化报错，说明抽象类是不能实例化的  ，

class Talker1(Talker): #如果抽象类的子类没有重写抽象方法，也是没法实例化的，必须重写抽象方法，才能实例化
	def speak(self,value):
		print('说了话',value);
	
	def talk(self):  
		pass;

talk1 = Talker1()

class Other:
	pass
o = Other()
# 这就就是把类Other变为Talker的子类啦。  这样会破坏继承的多态。所有不能使用这个 issubclass 和  isinstace  来检测对象啦，应该使用abc模块中的检测
Talker.register(Other)
print(o)

print(issubclass(Other,Talker))

print(isinstance(o,Talker))