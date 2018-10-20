from Handler import Handler
# html的文本生成的超类。
class HTMLRender(Handler):
    #输出开始解析文档的标签
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    #输出结束文档的解析标签
    def end_document(self):
        print('</body></html>')

    # 处于段落的开始
    def start_paragraph(self):
        print('<p>')
    # 处于段落末尾
    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')

    def start_url(self):
        print('<url>')
    def end_url(self):
        print('</url>')

    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')

    #处理文本的正则表达式  match：就是匹配了的字符串
    def sub_emphasis(self,match):
        #
        #print(match)
        return '<em>{}</em>'.format(match.group(1))
    #筛选超链接
    def sub_url(self,match):
        return '<a href="{}">{}</a>'.format(match.group(1),match.group(1))
    #筛选  邮件
    def sub_mail(self,match):
        return '<a href="mailto:{}>"{}</a>'.format(match.group(1),match.group(1))
    # 输出文本开始
    def feed(self,data):
        print(data)