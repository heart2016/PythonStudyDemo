#python 运行简单的服务器的方式 在cmd里面执行：python -m http.server --cgi   这样就表示会启动一个简单的http服务器。
#这个cmd走到那个路径下面，就表示那个当前路径就是  服务器的根目录，我们访问http://127.0.0.1:8000就会获取当前路径的文件目录
#这样启动的服务器，我们需要运行的程序，也就是服务器逻辑层的基本放在路径：cgi-bin中。所以我们新建一个first.py放入文件夹cgi-bin(当然这个cgi-bin也是需要新建文件夹的)

#记住：如果在文件夹中是新建了文件夹：cgi-bin 。那么该文件夹中的python的脚本需要以py后缀。并且访问方式是：

#http://127.0.0.1:8000/cgi-bin/first.py    first.py这个就是文件


print('这里记录的是怎么运行cgi服务器')