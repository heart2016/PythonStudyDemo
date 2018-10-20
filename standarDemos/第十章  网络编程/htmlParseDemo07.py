#屏幕抓取的时候，使用HTLMParse。
from urllib.request import urlopen
from html.parser import HTMLParser
class HTMLParseSample(HTMLParser):
	#用于标记某个标签是不是解析完了。
	in_link = False
	#当遇到标签的时候
	def handle_starttag(self,tag,attrs):
		print('遇到标签开始的调用=====>',tag,attrs)
		attrs = dict(attrs);
		#获得本标签的属性href属性的值
		url = attrs.get('href','')
		#表示已经进入的标签中
		self.in_link = True;
		#用来存放解析出来的文本的
		self.chunks = []
		
	#当遇到空标签，空标签的结束也会在这里调用
	def handle_startendtag(self,tag,attrs):
		print('空标签和结束标签都是这里调用=========>',tag,attrs)
		
	#标签结束调用
	def handle_endtag(self,tag):
		print('标签结束的方式======>',tag)
		if self.in_link:
			#表示标签解析完了
			self.in_link = False;
	
	#遇到文本数据是调用，这个文本数据要注意有可能不是一次加载出来，可能同一个文本数据需要调用几次才能加载出来
	#为了全部加载出来不乱，处理方式就是如下	
	def handle_data(self,data):
		#判断当前这个标签是不是走完了
		print('标签的文本数据=====>')
		print(data)
		if self.in_link:
			self.chunks.append(data)
		
	#遇到特殊字符调用
	def handle_charref(self,ref):
		print('遇到特殊字符调用如&#ref=======>',ref)
		
	#遇到引用的&name  获取其他引用的使用调用	
	def handle_entityref(self,name):
		print('引用名称是======>',name)
	
	#遇到注解的时候调用
	def handle_comment(self,data):
		print('注解是=====>',data
		)
	#遇到<!  >  这样的时候调用
	def handle_decl(self,decl):
		print('<!   >=======>',decl)
		
	#用于处理的指令
	def handle_pi(self,data):
		print('处理的指令=====>',data)
		
	#处理未知的声明
	def unknown_decl(data):
		print('未知声明=======>',data);
		
text = urlopen('http://python.org/jobs').read().decode()
parse = HTMLParseSample()
#指定需要解析的文本
parse.feed(text)
parse.close();