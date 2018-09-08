# 网络编程

#最简单的socket的学习   socket 客户端编程

import socket

s = socket.socket();

host = socket.gethostname();

print('服务器地址====》'+host);

port = 8081;
#发送连接请求到服务端
s.connect((host,port));
#这个是用于接收数据啦
print(s.recv(1024));