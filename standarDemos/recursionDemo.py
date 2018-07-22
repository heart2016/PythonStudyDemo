#函数作用于以及递归的学习

#函数作用于的学习
x = 10;
y = 20;
z = 30;
def changeX():
	x = 2; # 这样的x不会变化
	global y; # 这样的y才会变化
	y = 2;
	#z = 3;
	#global z;  这样会报错，会包前面已经定义了z，不能在定义了。所以使用全局变量global之后，就不能在定义一个同样名称的局部变量了。
changeX();
print(x,y,z);

#递归的函数，

#递归使用阶层的计算,计算n的阶层
def factorial( n = 1 ):
	if n == 1:
		return 1;
	else:
		return n*factorial(n-1);
print(factorial())  #计算阶层的函数。
print(factorial(10))  #计算阶层的函数。