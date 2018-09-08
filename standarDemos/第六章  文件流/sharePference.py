#  一个简单的数据缓存模块工具类

import sys,shelve  #  这样引入多个模块

# 让用户输入数据并且存入缓存文件中,传入的就是文件的 shelve对象，db就是这个对象
def insert_person(db):
	pid = input("请输入一个id，id是唯一的：");
	person = {}
	
	person['name'] = input('请输入这个人的姓名：');
	
	person['age'] = input('请输入年龄：');
	
	person['phone'] = input('请输入电话号码');
	
	db[pid] = person


#通过id  查看存放文件中的数据
def show_person(db):
	print('展示所有存放的信息：');
	pid = input('请输入需要查看人的id：');
	print(db[pid]);
	
def db_help():
	print('insert 命令是插入');
	print('show   命令是展示');
	print('quit   命令是退出')


# 合法化命令行
def enter_command():
	cmd = input('请输入命令行：')
	cmd = cmd.strip().lower();
	return cmd
	
def test():
	db = shelve.open('H:\\githubProject\\PythonStudyDemo\\standarDemos\\text01.txt')
	try:
		while(True):
			cmd = enter_command();
			if cmd == 'insert':
				insert_person(db);
			elif cmd == 'show':
				show_person(db);
			elif cmd == 'help':
				db_help();
			elif cmd == 'quit':
				break;
			else:
				continue;
	finally:
		db.close();

test();
	