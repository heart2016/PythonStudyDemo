#  数据库联系。在python3中使用的默认数据库是sqlite3。
# 如果sqlite3没有就需要安装 PySqlite

import sqlite3

def createTab():
	conn = sqlite3.connect('food.db');
	cur = conn.cursor();

	cur.execute('''
		CREATE TABLE food(
			id TEXT PRIMARY KEY,

			desc Text,
			water FLOAT,
			kcal FLOAT,
			protein Float,
			fat Float,
			ash Float,
			carbs float,
			fiber float,
			sugar float
		)

	''')
	conn.commit();
	conn.close();

def insertSample():
	conn = sqlite3.connect('food.db');
	cur = conn.cursor();
	insertString = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?)'
	#cur.execute(insertString,["11","11",11,11,11,11,11,11,11,11]);
	for item in range(1,10):
		cur.execute(insertString,[str(item),str(item),item,item,item,item,item,item,item,item]);
	conn.commit();
	conn.close();

def querySample():
	queryString = 'SELECT * from food ';
	print(queryString);
	#连接数据库。
	conn = sqlite3.connect('food.db');
	# 获得操作数据库的操作对象。
	cur = conn.cursor();
	cur.execute(queryString);
	# 这行代码是获得数据库中所有的列的名称，
	#cur.description 这个会获得一个二维元祖，元祖中还是一个元祖。元祖的每一个第一项才是我们要的列表名
	print(cur.description)
	# 把二维元祖的第一项，取出来放入一个列表中组成新的列表names。
	names = [f[0] for f in cur.description]
	print(names);

# 这就是查找出所有的数据，row代表的就是一行
	for row in cur.fetchall():
		#zip的作用是：压缩把zip（）里面的参数做成一个item，
		for pair in zip(names, row):
			print('{}:{}'.format(*pair))
		print();

#createTab();
#insertSample()
querySample();

