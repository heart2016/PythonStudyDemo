#网络编程
#下载网页资源的代码   
#在python3中使用的函数都是存在于：urllib.request中。


#from urllib.request import urlopen
import urllib.request
import re
example = 'https://github.com'
#简单的一个网页下载程序。使用的是 ：urlopen 
def firstDemo():
	#获得文本对象，这个就可以获取远端的文本对象
	webpage = urlopen(example);
	#读取所有文本
	text = webpage.read();
	print('文档是====>',text);
	print('============================================================')
	#正则表达式的筛选。
	m = re.search(b'<a href="([^"]+)".*?>.*</a>',text,re.IGNORECASE);
	print(m.group(1))
	
#firstDemo();

#获取远端的文本对象，并且可以缓存在本地
def secondDemo():
	#注意模块urllib中  网络函数urlopen和urlretrieve这些下载网络文件的函数都是存在于
	# urllib.request中。
	urllib.request.urlretrieve(example,'github.html');

secondDemo();