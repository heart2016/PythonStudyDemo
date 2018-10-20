#  绘制折线  其实就是使用对象PolyLine 这个类来绘制折线
from reportlab.graphics.shapes import Drawing,PolyLine

from reportlab.graphics import renderPDF

d = Drawing(400,400)
# 通过点生成需要绘制的线。  里面的都是点  坐标的方向是  竖直y  向上越大   水平x  向右越大
lines = PolyLine([(100,100),(200,0),(200,200)])
d.add(lines)

renderPDF.drawToFile(d,"line4.pdf"," line  file")