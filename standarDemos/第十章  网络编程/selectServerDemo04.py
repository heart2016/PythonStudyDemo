#网络编程

# 使用select 中的异步io来进程服务器的，也就是除了分叉和线程化外的第三种方式

#引入select，这个用来用做日志系统比较不错。是一个简单的日志系统的服务端。
import socket,select;

s = socket.socket();
#获取本地的socket地址。
host = socket.gethostname();
port = 8081;

#表示监听那个服务端地址，和端口号
s.bind((host,port));
s.listen(5);
#服务端s的集合，用来接收客户端的链接。
inputs = [s];
while True:
	#select.select(输入列表，输出列表，异常列表，超市时间)  本来是四个参数，第三个参数可有可无
	#返回值：rs，ws，es:这三个返回值是：输入列表，输出列表，异常列表
	rs,ws,es = select.select(inputs,[],[]) #这个方法是一个阻断的方法
	for r in rs:  #获得输入列表
		if r is s: #找出输入列表，找出就是和上面的s相等，就表示找出来了
			c,addr = s.accept(); #获得链接客户端的信息。
			print('地址是===>',addr);
			#把客户端的s加入到inputs中。
			inputs.append(c);
	else:
		try:
			data = r.recv(1024);
			disconnected = not data;
		except socket.error:
			disconnected = True;
				
		if disconnected:
			print(r.getpeername());
			inputs.remove(r);
		else:
			print(data)