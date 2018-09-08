# 服务器框架学习，python有很多服务器框架常用的有：TCPServer（支持TCP套接字流），UDPServer(支持UDP数据包套接字)，以及
# 难懂的UnixStreamServer ，UnixDatagramServer。   这些都是SocketServer的扩展类

#我们常用是：TCPServer，那么这个有很多扩展的框架：BaseHTTPServer，SimpleHttpServer等

#下面定义一个简单的服务器，启动了服务器，可以在客户端使用：localhost:8081访问

#  ForkingMixIn：分叉服务器
#ThreadingMixIn: 线程服务器

from socketserver import TCPServer,StreamRequestHandler,ThreadingMixIn;

class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername();
		print('====',addr);
		#这里就可以向客户端写出数据，记住这里的数据一定是要编码的，否者会报错
		self.wfile.write('谢谢你，访问服务器'.encode('utf-8'));
'''		
#这里是简单服务器也就是TCPServer的方式
server = TCPServer(('',8081),Handler);
#开启服务器。 运行了这里，在浏览器上面访问localhost:8081  就会有网页了，
server.serve_forever();
'''

'''
#window 系统不支持分叉，所以没法引入分叉的模块FockingMixIn
#所谓分叉，就是没来一个客户端就会开启一个进程的。
class FockingServer(ForkingMixIn,TCPServer):
	pass;
'''
	
# 这个是线程化的服务器，也就是多个客户端会有多个线程。
class ThreadingServer(ThreadingMixIn,TCPServer):
	pass;


server = ThreadingServer(('',8081),Handler);
#开启服务器。 运行了这里，在浏览器上面访问localhost:8081  就会有网页了，
server.serve_forever();