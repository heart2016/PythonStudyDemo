import fileinput

for line in fileinput.input(inplace = True):
	# line就是当前行的字符串，line.rstrip():去除前后的空白符
	line = line.rstrip()
	# 获得当前的行号
	num = fileinput.lineno();
	#  {:<5}  表示在line字符串后面，注意：当字符串不够5个时追加空格，多了5个直接在后面追加字符串  {：2d} 在字符串后面两个空格后追加整数
	print('{:<5}#{:2d}'.format(line,num))