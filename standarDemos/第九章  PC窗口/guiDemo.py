#简单的学习下布局的 GUI有空间的python

from tkinter import *;
from tkinter.scrolledtext import ScrolledText

def load():
	print('打开文件');
	with open(filename.get()) as file:
		contents.delete('1.0',END);
		contents.insert(INSERT,file.read())


def save():
	print('保存文件');
	with open(filename.get(),'w') as file:
		file.write(contents.get('1.0',END));

top = Tk();   # 这个一定是第一个T大写，k小写

top.title('选择要编辑的文件');

contents = ScrolledText();
contents.pack(side=TOP,expand=True,fill=BOTH);
filename = Entry();
filename.pack(side=LEFT,expand=True,fill=X);

Button(text='打开',command=load).pack(side=LEFT);
Button(text='保存',command=save).pack(side=LEFT);

mainloop()

