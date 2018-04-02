import csv
# 写入文件

with open('test.csv','w',newline='') as f:   #不加newline=''会多一个空行
    csv_writer=csv.writer(f,delimiter=',',dialect='excel')
    csv_writer.writerow(['列1','列2','列3'])
    data = [range(3) for i in range(3)]    #data 为一个列表,里面还有三个列表
    for item in data:
        csv_writer.writerow(item)

with open('test.csv','r') as f:
    csv_reader=csv.reader(f)
    for item in csv_reader:
        print(item)
