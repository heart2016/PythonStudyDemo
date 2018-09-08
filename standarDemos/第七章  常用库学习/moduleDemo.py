#第十章的 模块导入例子


def hello():
	print("模块化的例子")
	
	

def test():
	hello();
	print('用来测试的');
print("module",__name__)  # 当模块当作一个主程序的时候：__name__  的值就是 __main__;   但是如果模块就是当着模块的时候，那么__name__就是模块名了 

if __name__ == '__main__': test()