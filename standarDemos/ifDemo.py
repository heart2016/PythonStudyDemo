# 这里就可以看出，python一定是要缩进对号，缩进不对，python解释器会报错的。
if(0):
	print("打印了0");
else:
	print("else")
	if 0:
		print("结束")
	else:
		print("shabi")
#这里就是检测  is  和  == 的区别。  可以看的出来 is是检测对象是不是同一个地址，== 只要判断对象是不是相等就够了
x = y = [1,2,3]
z = [1,2,3]
w = x.copy();
#输出的值是：	True，	True，  True，	False，		True，		 False
print(				x==y,	 x is y, x == z, x is z,   x == w ,   x is w) 
#比较，看看字符串的比较 :  是一个一个字符拿出来比较，比如A 与 B 两个字符串比较，或按索引先拿出0  如果索引0  就不是一样的  那么这两个字符串的大小就确定了。列表也是这样比较大小的
print("ruu" < "retet",ord("a"),ord("r"))

#一个例子
number = input("请输入一个1-10的数字：");
if number.isnumeric(): #检测输入是不是数字
	num = int(number); #强转为数字
	if 1<=num<=10: #判断
		print('Greet');
	else:
		print('Wrong')
else:
	print('请输入数字');
	