#Python的抽象学习笔记

#定义一个函数的方式：
def hello(name):
	return "this is  your name : "+name;
	
#一个返回一连串斐波拉序列的数组的函数：斐波拉序列数就是：前两个数的和等于第三个数的值。
def feiArray(n):
	result = [0,1];
	for i in range(n-2):
		# 这就是获得列表的最后一个数  和  倒数第二个数。记住在python的列表的倒叙迭代取值。
		num = result[-1] + result[-2]
		result.append(num);
	return result;
	
print(hello("傻逼"),feiArray(10))

#这样定义的两个参数。也可以制定默认值.
def keyParams(name,number):
	print("名字是：{},数字是：{}".format(name,number))
keyParams('hah',20)
#这样指定  所谓的关键字参数，就不必在意参数的顺序了。也是可以调用的
keyParams(number=40,name='uu')  #打印的是：名字是：uu,数字是：40
#keyParams(number=10)   这样会报错，应为是两个参数，我们值传递了一个参数

#指定默认值的函数：这样就可以指定必须传递的参数，有默认值得是：可选传递的参数（也就是可以传递，也可以不传递）
def keyParams_m(name = '静静',number = 10):
	print("名字是：{},数字是：{}".format(name,number))	
keyParams_m(); #但是指定了默认参数，我们就可以传递的参数可以传递，也可以不传递
keyParams_m(None,None)  #打印的是：名字是：None,数字是：None

#可变参数的指定 *param：这样表示可以传递0个参数，或者更多参数，传递的参数在函数体里面获取就是一个元祖啦
def changeParams1(*param):
	print(param)
changeParams1();
changeParams1(10,'iiii');

#有了可变参数，还要再加上其他参数，调用的时候只能那种：changeParams2(88,name=90);  关键字调用，否者报错
def changeParams2(*param,name):
	print(param)
changeParams2(88,name=90); #这个不会报错的。
#changeParams2(30,'eeee');  #这个是会报错的。

# 这样调用的时候一定要使用关键字调用。否者就会报错。所以后面的打印的出来的是：字典不是元组。
def changeParams3(**param):
	print(param)
changeParams3(time=88,name=90); #这个不会报错的。
#changeParams3(44); #这个会报错的。使用**params  一定要使用关键字参数的形式