#异常的学习Demo

#多个这样的异常，只会有一个执行，当前面的执行了，就会终止后面的代码块。这样代码就不会在走下去了
run = False
if run:
	try:
		x = 10
		raise TypeError
		y = 0
		z = x/y
	except ZeroDivisionError:
		print('除数为0异常')
		raise TypeError  #在这里抛出的异常不会再被下面的补货，除非外层还有一个try：  except
	except TypeError:
		print('类型异常')

#异常重定向
if run:
	try:
		x = 10
		raise TypeError
		y = 0
		z = x/y
	except ZeroDivisionError:
		print('除数为0异常')
		raise TypeError
	except TypeError:
		print('类型异常')
	
#异常直接的父类与子类问题
run = False
if run:
	try:
		x = 10
		y = 0
		z = x/y
	except Exception: #只会捕获这里的异常，后面的子类异常走不到，这是由于所有的异常都是Exception的子类。
		print('除数为0异常')
	except ZeroDivisionError:
		print('类型异常')
		
#想一次捕获多个异常的用法
run = False
if run:
	try:
		x = 10;
		y = 0;
		z = x/y;
	except(ZeroDivisionError,TypeError,NameError): #这样这个except就可以捕获很多异常了。也就是里面的三类异常了
		print('捕获了三类异常中的一种')
		
#捕获了异常的异常对象获得方式
run = False
if run:
	try:
		x = 10;
		y = 0;
		z = x/y;
	except(ZeroDivisionError,TypeError,NameError) as e: #这样就得到了当前捕获的异常对象
		print('捕获了三类异常中的一种=====>'+e)  #  这样打印出来是不行的，打印不出来。以为e不是str。
		
		
#try:  except :  else:
run = False
if run:
	try:
		x = 'a';
		y = 1;
		z = x/y;
	except(ZeroDivisionError) as e: #这样就得到了当前捕获的异常对象
		print('捕获了三类异常中的一种=====>') 
	else:
		print('执行了else');  #只有没有异常发生。才会执行下面的else
		
#try:  except :  else:  finally:
run = False
if run:
	try:
		x = 10;
		y = 1;
		z = x/y;
	except(ZeroDivisionError) as e: #这样就得到了当前捕获的异常对象
		print('捕获了三类异常中的一种=====>') 
	else:
		print('执行了else');  #只有没有异常发生。才会执行下面的else
	finally:
		print('执行了finally语句')  #发生异常会执行这个语句，没有发生异常也会执行该语句
		
def testException():
	try:
		x = 10;
		y = 1;
		z = x/y;
		print('返回',z)  # 这里会执行
		return z;
		print('===============') #不会执行
	except(ZeroDivisionError) as e: #这样就得到了当前捕获的异常对象
		print('捕获了三类异常中的一种=====>') 
	finally:
		print('执行了finally语句')  #就算前面返回了，这里也会执行
print('执行代码============')
testException()
print('结束代码============')

#警告示例代码:
from warnings import warn
warn('提出一个警告')

warn('提出一个警告')
warn('提出一个警告')