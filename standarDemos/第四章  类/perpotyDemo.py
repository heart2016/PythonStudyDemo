#使用 Perpoty的方法

class student:
	
	def __init__(self, name,age):
		self.name = name;
		self.age = age;
	
	def set_id(self,id):
		self.name = id;
	def get_id(self):
		return self.name;
		
	def set_start(self,start):
		self.age = start;
	def get_start(self):
		return self.age;
		

	id = property(get_id,set_start)

stu = student(name='小明',age=10);


print(stu.name,stu.age)

print(stu.id)
stu.id = 100
print(stu.age,stu.id)