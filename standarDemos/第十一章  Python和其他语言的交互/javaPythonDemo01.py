# -*- coding: utf-8 -*- 

'''
上面的第一行代码：# -*- coding: utf-8 -*-    这也是为了指定当前的编码格式utf-8
这里就是引入的java类，这个文件必须使用jython运行。否者无法运行。
jython 我们必须安装，就是下载jython的jar包  下载好了之后再cmd中运行：java -jar 下载的jar包的绝对路径以及名称
这样就会弹出安装选项对话框
'''
import javaDemo

test = javaDemo()

print('哈哈哈')

test.hello();