#!/usr/bin/python
#coding: utf-8

import xlsxwriter

workbook = xlsxwriter.Workbook('图表的创建.xlsx')
worksheet = workbook.add_worksheet()


#先创建add_chart---再chart.add_series或insert_char
#新建图标对象
chart = workbook.add_chart({'type': 'column'})

#向 excel 中写入数据，建立图标时要用到
data = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
]

#将列表指定开始单元格写入一整列
worksheet.write_column('A1', data[0])
worksheet.write_column('B1', data[1])
worksheet.write_column('C1', data[2])

#向图表中添加数据，例如第一行为：将A1~A5的数据转化为图表
#分别增加三个系列的数据
chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

#将图标插入表单中
worksheet.insert_chart('A7', chart)

workbook.close()