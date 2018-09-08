#网络编程

#使用Twisted，这个是一个事件驱动的服务端框架,我们需要安装一个Twisted  安装的方式就是：
#第一步：访问：https://www.lfd.uci.edu/~gohlke/pythonlibs/  ，找到我们需要的后缀是whl的文件，注意平台的选择，
#举个例子：pip install C:\Users\Administrator\Downloads\Twisted-18.7.0-cp37-cp37m-win32.whl    cp37m：表示python的版本号是3.7.0  win32：表示是inter处理器
#					win-amd64：表示amd的处理器
#第二部就是  pipi install 绝对路径   就可以了
#一个简单的日志服务器。
from twisted.internet import reactor;
from twisted.internet.protocol import Protocol,Factory;
from twisted.protocols.basic import LineReceiver;
class SimpleLogger(Protocol):
	#当有客户端链接是调用
	def connectionMade(self):
		print("有新的链接的回调====》",self.transport.client);
		
	#当有客户端掉了链接的回调
	def connectionLost(self,reason):
		print('又来链接断掉====>',self.transport.client);
		
	#接收到数据的回调
	def dataReceived(self,data):
		print('接收到的数据',data);
		
#这个是使用了协议LineReceiver改进后的日志服务器  
class SimpleLineLogger(LineReceiver):
	
	def connectionMade(self):
		print("有新的链接的回调==11==》",self.transport.client);
		
	def connectionLost(self,reason):
		print('又来链接断掉==11==>',self.transport.client);
		
	def dataReceived(self,data):
		print('接收到的数据111',data);
		self.transport.write("哈哈哈哈".encode('utf-8'))

# 实例化一个工厂,这个工厂用处是：当有一个新连接到来时会创建一个协议对象
factory = Factory();
#factory.protocol = SimpleLogger;
# 指定工厂里面的协议类，也就是当前服务器服从的协议类。
factory.protocol = SimpleLineLogger;

#  监听端口和创建协议对象的工厂
reactor.listenTCP(8081,factory);
reactor.run();