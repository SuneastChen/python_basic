import xlrd
data = xlrd.open_workbook('abc.xlsx')
table = data.sheets()[0]  # 通过索引获取sheet表
# table = data.sheet_by_index(0) #通过索引
# table = data.sheet_by_name(u'Sheet1')#通过名称

datalist1 = table.row_values(2)  # 获取整行数据
print(datalist1)
datalist2 = table.col_values(0) #获取整列数据
print(datalist2)

nrows = table.nrows
print(nrows)  # 获取行数
ncols = table.ncols
print(ncols)  # 获取列数

# 循环打印每一行数据
for i in range(nrows):
    print(table.row_values(i))

# 获取单元格的内容
cell_a1 = table.cell(0,0).value
print(cell_a1)

cell_a2 = table.col(1)[0].value
print(cell_a2)
cell_b2 =table.row(1)[1].value
print(cell_b2)