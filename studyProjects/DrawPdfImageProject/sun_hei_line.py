# 真正练习  太阳黑子的生成文件

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
#	第一项 第二项	第三项  第四项  第五项
#	年份  月份   厉害度		 最高    最低
	(2007,8	,			113.2,	114.2,	112.2),
	
	(2007,9,112.8,	115.8,	109.8),
	
	(2007,10,		111.0,	116.0,	106.0)
	,
	
	(2007,11,	109.8,	116.8,	102.8)
	,
	(2007,12,107.3,	115.3,	99.3)
	,
	(2008,1 , 105.2,	114.2,	96.2)
	,
	(2008,2,		104.1,	114.1,	94.1)
	,
	(2008,3,	99.9,	110.9,	88.9)
	,
	(2008,4,94.8,	106.9,	82.8)
	,
	(2008,5,		91.2,	104.2,	78.2)
]

#设定画布的宽高
drawing = Drawing(200,150)
#求取的是：data里面的 第三项 - 40  做成的一个集合
pred = [row[2]- 40 for row in data]
height = [row[3]- 40 for row in data]
low = [row[4] - 40 for row in data]
times = [200*((row[0]+ row[1]/12.0) - 2007)-110 for row in data]

drawing.add(PolyLine( list( zip(times,pred) ) , strokeColor=colors.blue));
drawing.add(PolyLine(list( zip(times,low) ),strokeColor=colors.red));
drawing.add(PolyLine( list(zip(times,height) ),strokeColor=colors.green));

renderPDF.drawToFile(drawing,"report4.pdf","sun_hei_line")