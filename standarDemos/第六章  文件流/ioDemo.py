# 使用io模块  对于io模块  这个模块是默认导入的。也就是默认模块

import sys;

#写入文件
def onlyWrite():
	f = open('ioDemoFile.txt','w')  #两个参数，第一个是文件路径，没有路径，就是代码所在文件夹。第二个参数，但是：w  表示本次写入会覆盖整个文件。
	for i in range(1,101):
		f.write('Hello world IO');
		f.write(str(i));  #这个是把整形转化为字符串，  字符串转化为整形 ： int(str_num)
		f.write('\n');
	
	f.write('Hello world IO\n');
	
	f.write('傻逼啊   傻逼');
	f.flush()
	f.close();
#读取文件数据	
def onRead():
	f = open('ioDemoFile.txt','r')

	print("====>"+f.read(4));
	
	print(f.read());
	f.close();
	
#使用我呢见迭代器： 语法是：with  open(文件名) as f:  后面就可以使用f就是文件对象了。使用这个的优势是不需要关闭流，自动会帮助关闭
def userWith():
	with open('ioDemoFile.txt','r') as f:
		for line in f:  #  这个会把所有的文件都读取出来，一行一行的读取，到没有数据为止
			print(line);

#使用不是with的方式，把数据一行一行迭代出来
def userOlder():
	f =  open('ioDemoFile.txt','r');
	while True:
		line = f.readline();
		if not line:
			break;
		print(line);

# 使用标准流，print  把数据写出到文件中
def printInFile():
	f = open('printFile.txt','w');
	print('啊哈哈哈哈',file=f);  #这样的输出就会重定向，就会输出到文件中
	print('两个参数','第二个参数',file=f);
	print('三个参数','三个参数','三个参数',file=f);
	print('==================',file=f);
	print('结束')
	f.close();
	
	with open('printFile.txt','r') as fIn:
		for line in fIn:
			print(line);
	
			
	
#onlyWrite();

#onRead();

#userWith();

#userOlder();

printInFile();