#  正则表达式的学习

import re

#  通过模块re,获得一个模式，也就是正则的模式
def compile_Demo():
	pat = '.ython';
	return re.compile(pat);  #  这样就是会返回一个模式。通过一个字符串返回一个模式

#  模块的方法：re.split(正则表达式字符串，需要分割的字符串)   返回值是一个集合  使用正则表达式分割字符串
def patter_split():
	pat = '[,]+'  #表示最少一个逗号，多个也行，但不能没有
	
	exString = 'hahah,,,,,  hahahha,huuuu,9傻逼,韩货,夯实';
	
	result = re.split(pat,exString);
	print(result)
	
#  re.findall(正则模式，字符串) 返回值是一个集合  返回在字符串中查到符合的子字符串  
def patter_findAll():
	
	pat = '[a-zA-Z]+'
	
	exString = 'hello  大家   wo shi  english';
	
	result = re.findall(pat,exString);
	print(result)
	print(len(result))
	
	
def patter_group():
	pat = r'www\.(.*)\..{3}';
	# 这个模板:r'www\.(.*)\.(.{3})'  这个是分了3个组：第一个组是字符串的整体，第二个组就是小括号内的 .* 到 后面的\.的转义为第二组  第三组就是：.{3}
	#  如果是模板：r'www\.(.*)\..{3}';  这个是只分两两个组; 第一组：整个字符串； 第二组也就是：.*  ，如果没有后面的\. 表示这个字符一定要存在
	exString = 'www.python.org'
	
	m = re.match(pat,exString)
	print(m.group())   # 代表的就是整个字符串，也就是exString
	print(m.group(0))		#  代表的就是整个字符串的匹配，也就是exString
	print(m.group(1))  # 这个代表的就是匹配
	print(m.start(1)) # 输出  4
	print(m.end(1));  # 输出 10
	print(m.span(1)); # 输出 (4,10)
	
	#print(m.group(2))  #输出 .org
	
	#print(m.start(2)) # 输出11
	#print(m.end(2))  # 输出  14
	
	#print(m.span(2)) # 输出（11，14）

# 用来置换，字符串  re.sub(正则模式，置换那个组,需要置换的字符串)

def sub_group():
	pat = r'\*([^\*]+)\*'  #  这个正则表示 组号1  是不是以  *开头的字符，长度任意
	exString = 'Hello, *1111* *word * !';
	
	result = re.sub(pat,r'<em>\1<em>',exString);  #  这里的\1 表示替换的是group（1）   也就是组1.
	
	print(result)
	
def module_patter():
	pat = re.compile(r'\[(.+?)\]');  # 这个一定要是  .+?  要是顺序反了就会报错
#	pat = re.compile('.*')
	#print(pat)
	exString = '1 and 2 is [1+2]'
	print(exString)
	#m = re.Match(pat,exString);
#	print(m)
	re.sub(pat,repalce_ment,exString)  #  中间的参数有点类似于回调的感觉。回调的参数是一个MatchObject啦	
	#print(pat.sub(repalce_ment,exString))#  这个是上面的简化版
	
	
	#result = re.sub(pat,eval('\1'),exString);
	
	#m = re.match(pat.group(1),exString)   # 这样不行
	#print(m)
	
	#print(result)
	
def repalce_ment(match):
	print('match:')
	print(match)    # 这个是  <re.Match object; span=(11, 16), match='[1+2]'>
	code = match.group(1)
	print('code:')
	print(code)  #  这个是  1+2
	print(eval(code))  #  这个方法会把 1+2  计算出来
	try:
		return str(eval(code,scope));
	except SyntaxError:
		return ''
scope = {}
def test_Demo():
	m = compile_Demo().match('python');  #  这样会获得一个Match对象，通过这个可以匹配的东西
	print(m)
	
	print('==========下一个===================')
	patter_split();
	
	print('=========下一个==========')
	patter_findAll()
	
	print('========下一个==========')
	patter_group();
	
	print('========下一个==========')
	sub_group();

	print('========下一个==========')
	module_patter()
	
test_Demo();