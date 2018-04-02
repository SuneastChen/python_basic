
print('-------------------创建文件--------------------')

f=open('g:\\text.txt','w')     # 必须加:\\  只能是'a'(打开原有,末尾加入)或'w'(创建一个新的,原有被覆盖)
f.write('1234567890\n')       #写入文件
b1=[99,88,77,'我爱你','世界!']
for i in b1:
    f.write(str(i))        #必须转成字符串才能写入

f.writelines('\n任何不足以致命的痛苦必将使你成长!')   #与f.write()相同
f.write('人生如戏,何必在意,认真你就输了这世界!')

print(f.tell ())       #返回当前指针位置
f.seek(10,0)           #移动指针,后一个参数,0代表起始位置,1代表当前位置,2代表文件末尾
f.write('<我是后加入的>')    #w模式,用取代模式写入,a模式则会在末尾写入

f.close()

print('-------------------读取文件1,这种方法不好用--------------------')

f=open('g:\\123.txt')    #默认只读方式打开

while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line) 


f.close()

print('-------------------读取文件2--------------------')
f=open('g:\\123.txt')

for line in f:
    print(line)

f.close()

print('-------------------读取文件3--------------------')
f=open('g:\\123.txt')

##a1=f.readline()           #只能读取一行,不可加参数,否则按字符串个数读取
a2=f.read()             #读取文件,好用
a3=f.read(-1)             #括号加数字参数,代表读出几个字符,-1代表接着读取剩余

##print(a1)
print(a2)
print(a3)

f.close()



print('-------------------with 打开文件,不用关闭--------------------')
with open('g:\\123.txt')as f:
    a4=f.read()
    print(a4)






















