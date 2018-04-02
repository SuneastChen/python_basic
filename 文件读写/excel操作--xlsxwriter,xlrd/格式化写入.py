
#!/usr/bin/python
#coding: utf-8

from datetime import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook('格式化写入.xlsx')
worksheet = workbook.add_worksheet()

#设定格式，等号左边格式名称自定义，字典中格式为指定选项
#bold：加粗，num_format:数字格式
bold_format = workbook.add_format({'bold':True})
money_format = workbook.add_format({'num_format':'$#,##0'})
date_format =workbook.add_format({'num_format':'mmmm d yyyy'})
# ecxel 中每一个单元，如下属性都可设置：字体（fonts）、颜色（colors）、模式（patterns）、边界（borders）、alignment、number formatting

#还可用对象接口设置格式属性
money_format.set_font_color('red')
#xxx_format.set_bold()


#将第二行第二列(B2)设置宽度为15(从0开始)
worksheet.set_column(1, 1, 15)

#用符号标记位置，例如：A列1行
worksheet.write('A1', 'Item', bold_format)
worksheet.write('B1', 'Cost', bold_format)
worksheet.write('C1', 'Cost', bold_format)

expenses = (
    ['Rent', '2016-03-11', 1000],
    ['Gad',  '2016-03-12',  100],
    ['Food', '2016-03-13', 400],
    ['Gym',  '2016-03-14',  50],
)

row = 1
col = 0

for item, date_str, cost in (expenses):
    #将date_str  转化为Python datetime.datetime 格式
    #之后用write_datetime方法录入日期格式
    date = datetime.strptime(date_str, "%Y-%m-%d")

    #使用write_string方法，指定数据格式for循环写入数据
    worksheet.write_string(row, col,     item)
    worksheet.write_datetime(row, col + 1, date,  date_format)
    worksheet.write_number(row, col + 2, cost, money_format)
    row += 1


worksheet.write(row, 0, 'Total',       bold_format)
worksheet.write(row, 1, '=SUM(B2:B5)', money_format)

workbook.close()