from reportlab.graphics.shapes import Drawing,String

from reportlab.graphics import renderPDF
# 设定画布的宽高。   
d = Drawing(1000,1000)

# 在坐标  500，500  的位置写入字符串。
s = String(500,500,"hahahhaha",textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d,"hello3.pdf",'a simple pdf file')