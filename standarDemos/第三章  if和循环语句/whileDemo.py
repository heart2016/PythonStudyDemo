#循环语句的学习
x = 1;
while x < 100:
	print("=====>{}".format(x));
	x += 1;
#for循环打印字符串
x = "Hell0 World";
for item in x:
	print(item);
#for 循环可以获得 索引和元素的方式	
for i,item in enumerate(x):
	
#推导

	print(i,item)
	
#说明for  else   
#说明，就算是有contiune  也算是正常退出循环，会执行else
for item in x:
	if item == 'W':
		#continue;#当时continue 会执行后面的else  ，说明continue也算是正常退出循环
		break; #  break  不是正常退出循环，所以不会执行后面的else。
	print(item);
else:
	print("执行了for===els");
	
t = True
while t:
	word = input("请输入一个数组：");
	if word == 'e':
		t = False;
	print("输入的是",word);
else:
	print("输出while的else");  # 这样也会输出else。但是如果用break就不行的，就不会输出这个else
	
#推导  range(1)  就是获得0 -1  但不包括1。
b = [(x,y,z) for x in range(1) for y in range(2) for z in range(3)]

#exec 执行 exec('字符串')  把字符串参数当着代码执行。
exec("for x in range(10): print(x)")  #这就是执行 字符串代码
