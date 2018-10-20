import sys,re

from Handler import *
from HTMLRender import HTMLRender
from Rule import *
from HeadingRule import *
from TitleRule import *
from ListItemRule import *
from ListRule import *
from ParagraphRule import *
from Parse import Parse

class BasicTextParase(Parse):
    def __init__(self,handler):
        Parse.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*','emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')
print('================================')
handler = HTMLRender()
parser = BasicTextParase(handler)
parser.parse(sys.stdin)
