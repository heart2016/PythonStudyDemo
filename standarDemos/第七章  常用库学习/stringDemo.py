#String的学习例子代码

# 记住  字符串没有 sort方法，也没有：list(1,2,3)  这是不合法的方法。
b = '-'.join('Heoop')  #生成 H-e-o-o-p
print(b)

#当一个字符串排序，但是大小写不同或影响字幕的排序方式，可以用下面的方式
a = 'BzaCD'
# 这样使用key指定排序的规则是，字符都变为小写后排序
b = sorted(a,key = str.lower)
#获得排序之后的字符串：['a', 'B', 'C', 'D', 'z']
print(b);
