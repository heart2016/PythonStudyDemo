# 使用三个引号（单引号，双引号都可以） 后面的换行符，输出也会换行,转义字符\n等  也会换行，
print(""" hahhaha

aajhjdhjfh\ndj


ajdkfajsdhfj '你好'


！！！！'不好'

""")

# 下面的会报错，是由于有了换行的因素  这个回车报了错
#print(" hahhahaaajhjdhjfhdj   ！！！！！'你好' lllll '不好'

#ajdkfajsdhfj '你好'


#！！！！'不好'
#")

#这个多个引号不会报错
print(" hahhahaaajhjdhjfhdj   ！！！！！'你好' lllll '不好'")


# 这样就是原始字符串，原始字符串，是以r开头，后面是单引号或者双引号   。
#原始字符串注意两点： 里面不能有  let's go  不成对出现的单引号或者双引号  不能以\结束
print(r"let\'s go");  # 这个是合法的，不违背第一条




