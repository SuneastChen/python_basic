#coding:utf8
import xlsxwriter
import datetime,time

#创建一个新的xlsx文件(如果原有同名文件会被覆盖)
workbook = xlsxwriter.Workbook(r'.\xlsxwriter基本使用.xlsx',{'strings_to_numbers':True})
#{'strings_to_numbers':True} 写入数字字符串时是否转换成数字
worksheet = workbook.add_worksheet('test') 
#创建一个excel文件的工作表,括号为空就是默认名"sheet1"


#特别注意,"A2"引用单元格位置,必须大写字母,否则报错
worksheet.set_column('A:A',25) #定义A列宽度为80
bold = workbook.add_format({'bold':True}) #定义一个加粗的格式

worksheet.write('A1','Hello')
worksheet.write('A2','Word',bold) #A2中的内容为粗字体
worksheet.write('F1','中华人民共和国')
worksheet.write('B1',u'哈哈')
worksheet.write('B2','呵呵')
worksheet.write(7,1,33) #在B列 第8行插入数字33(行与列从0开始算)
worksheet.write(8,1,55)
worksheet.write(9,1,'=SUM(B8:b9)')
worksheet.write_string(2,0,'aaa') #在A3处插入字符串 aaa
worksheet.write_number('A4',234) #在A4处插入数字234
worksheet.write_blank('A5',None) #在A5插入一个空值
worksheet.write_formula('C10','=SUM(B8:B9)') #写入一个加法公式
#worksheet.write_datetime(17,3,datetime.datetime.strptime('2015-07-16','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))
                        #插入的位置;数据;格式
#worksheet.write_boolean(0,0，True) #写入逻辑类型数据
worksheet.write_url('A6','http://www.allyes.com') #url
worksheet.set_row(10,100.1,None,{'level':True}) #第一项是行号0开始计算，第二项是高度支持小数点，第三项是格式化，第四项是：hidden 隐藏 level 组合分级 collapsed 折叠
worksheet.set_column('E:G',None,None,{'hidden':1}) #隐藏E到G 设置一列以上的单元格属性
worksheet.insert_image('M1','G:\\IT笔记\\python实例\\999.jpg') #在C10这个位置插入图片a.png
#worksheet.insert_image('B55','e:\\a.png',{'url':'http://www.baidu.com'}) #在B55位置上插入a.png图片并附带地址






#表格制图

worksheet.write(29,0,13)
worksheet.write(30,0,25)
worksheet.write(31,0,63)
worksheet.write(32,0,103)
worksheet.write(33,0,32)

#先创建add_chart---再chart.add_series或insert_char
chart = workbook.add_chart({'type':'column'}) #创建图表类型是圆柱形
#column 柱状图
#area 面积图
#bar 条形图
#line 折线图
#radar 雷达图

worksheet.insert_chart('B30',chart) #将图表插到B30这个位置上
chart.add_series({
    'categories':'=test!$A$30:$A34',  #标签的范围,相当于系列的名称
    'values':'=test!$A$30:$A34', #获取A30-A34上的数据做入列表中
    'line':{'color':'red'}, #颜色是红色
})    #此为增加一个系列的数据


chart.set_x_axis({
    'name':u'x轴名', #x轴的名字
    'name_font':{'size':14,'bold':True}, #设置轴名称的大小是14并且加粗
    'num_font':{'italic':True}, #x轴名称字体,颜色
})
chart.set_y_axis({
    'name':u'y轴名', #设置y轴名称
    'name_font':{'size':14,'bold':True}, #设置y轴名称的大小是14并且加粗
    'num_font':{'italic':True,'color':'red'}, #数字字体，斜体
})
chart.set_size({  #设置图表整体的大小
    'width':500, #宽
    'height':550,#高
})
chart.set_title({       #整个图表的标题 显示在圆柱形图上方
    'name':u'图表标题',
})
chart.set_style(16) #就是图形整体的颜色和样式

chart.set_table() #在x轴下方设置表格,显示数据
chart.show_hidden_data()

workbook.close()