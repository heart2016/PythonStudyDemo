# 简单的抓取网页的程序。也就是下载网页

from urllib.request import urlopen
import re

# 这是简单的使用正则表达式来匹配网页，寻找有用的信息
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
# 获取远端的网页，并且解码。

text = urlopen('http://python.org/jobs').read().decode();
for url ,name in p.findall(text):
	print('{},{}'.format(name,url))