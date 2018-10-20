#屏幕抓取，使用Beautiful Soup的库来抓取网页数据

#要是用beautiful soup  需要载入某个库。载入方式：在cmd中运行：pip install beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/jobs').read().decode();
#实例化BeautifulSoup,这样就是获得封装了text的BeautifulSoup对象。
soup = BeautifulSoup(text,'html.parser')

jobs = set()
#获取在某个标签中的数据，这里是获取到body中在h2标签中的数据
html_h2 = soup.body.section('h2');

print(html_h2)

for job in html_h2:
	#  这个就是获得h2  中第一个出现的a标签a.string 就是表示a标签括起来的文本
	print('a=====>{}'.format(job.a.string))
	#获得a标签的属性href的值
	print('a（href）======>{}'.format(job.a['href']));
	jobs.add('{}   {}'.format(job.a.string,job.a['href']))
	
print('=============排完序的打印处理啊==================')
#对列表中的值进行排序，排序的规则是字符串，并且字符串都变成小写
print('\n '.join(sorted(jobs,key=str.lower)))