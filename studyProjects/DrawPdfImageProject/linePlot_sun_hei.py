#  使用LinePlot来绘制曲线图

# 真正练习  太阳黑子的生成文件
from urllib.request import urlopen
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
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

data = []
#读取网络文件
for line in urlopen('ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt').readlines():
	#解码行数据
	line = line.decode()
	print(line)
	#过滤行的条件：不能全是空格  并且  第一个字符不能包含 #；两个字符中的任何一个
	if not line.isspace() and line[0] not in '#:':
		#float(n)  表示类型转换
		data.append([float(n) for n in line.split()])

#设定画布的宽高
drawing = Drawing(400,200)
#求取的是：data里面的 第三项 - 40  做成的一个集合
pred = [row[5] for row in data]
height = [row[6] for row in data]
low = [row[7] for row in data]
times = [(row[0]+ row[1]/12.0) for row in data]

lp = LinePlot()

# 跨度  设定 x,y的跨度  这个是
lp.x = 50
lp.y = 50

lp.height = 125
lp.width = 300

lp.data =[
	list( zip(times,pred)),
	list( zip(times,low)),
	list(zip(times,height))
] 

#设定颜色
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.green
lp.lines[2].strokeColor = colors.red	

drawing.add(lp)

s = String(300,150,"support",fontSize=14,fillColor=colors.red)
drawing.add(s)
renderPDF.drawToFile(drawing,"support4.pdf","sun_hei_line")