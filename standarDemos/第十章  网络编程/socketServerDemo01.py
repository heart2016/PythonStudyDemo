#网络编程  
#这里学习网络编程最基础的知识 socket  server  服务端

import socket

# 获得套接字
s = socket.socket();

host = socket.gethostname();
print('服务器地址'+host);

port = 8081;
#绑定地址和端口：  host 这个是当前运行程序的地址，
s.bind((host,port));

#等待连接的队列中最多5个
s.listen(5);
print('开始for循环了')
while True:
	#等待客户端的链接
	print('开始等到客户端连接')
	#  当有客户端的时候就会产生一个链接。返回值是一个元祖，第一个就是用于操作的类，还有一个是客户端的地址:addr。
	c,addr = s.accept();
	print('获得一个客户端连接');
	#print(c);
	print(addr);
	#这里只能使用send 和 sendall  发送字节，所以只能使用encode('utf-8')编码成字节
	c.send('Hello world '.encode('utf-8'))
	c.close();
	