"""
第一行注释内容
第二行注释内容
第三行注释内容
单双引号都可以注释
"""
#a1=raw_input('请输入用户名:')    #py2.0适用,3.0报错
#a1=input('请输入用户名:')

##import getpass        #未安装此模块
##a2=getpass.getpass('请输入密码:')

'''
if 条件:
    执行代码
else:
    执行代码



if 条件:
    执行代码
elif:
    执行代码
elif:
    执行代码
else:
    执行代码



while 条件:
    代码块
    if 条件:
        break或continue

'''

import time
a2=0
while a2<3:
    a2+=1
    print('a2=',a2)
    time.sleep(1)



a3='陈旭东'   #utf-8编码
a3_unicode=a3.encode('utf-8')    #utf-8转unicode
print (a3_unicode)    #b'\xe9\x99\x88\xe6\x97\xad\xe4\xb8\x9c'
a3_gbk=a3.encode('gbk')     #utf-8转gbk
print(a3_gbk)         #b'\xb3\xc2\xd0\xf1\xb6\xab'



name='陈旭东'
for i in name:
    bytes_list=bytes(i,encoding='utf-8')
    #print(bytes_list)     #每个汉字为三个  16进制数
    for b in bytes_list:
        #print(b)          #每个汉字为三个 10进制数
        print(bin(b))     #每个汉字为三个  8位 2进制数
#字符-->16进制-->10进制-->2进制


#utf-8下字符串与字节的相互转换
print(str(b'\xe4\xb8\x9c',encoding='utf-8'))     #16进制-->字符'东'

print(str(b'\xe9\x99\x88\xe6\x97\xad\xe4\xb8\x9c',encoding='utf-8'))  #陈旭东

print(bytes('陈旭东',encoding='utf-8')) #b'\xe9\x99\x88\xe6\x97\xad\xe4\xb8\x9c'






print(9/2)    #4.5


a4='123456'
print(len(a4))     #6,实际个数

a5=['a',2,'b',4,'c',6]
print(len(a5))     #6,实际个数


for i in a5:
    print('第'+str(i)+'个位置的元素是:'+str(i))






a6=[11,22,33,44,55,66,77,88,99]
a7={'k1':[],'k2':[]}
for i in a6:
    if i<50:
        a7['k1'].append(i)
    else :
        a7['k2'].append(i)
print(a7)              #{'k1': [11, 22, 33, 44], 'k2': [55, 66, 77, 88, 99]}



a7=['a','b','c','d']
a8='#'.join(a7)
print(a8)       #      #a#b#c#d


a9='chenxudongshihaoren'
a9.partition('dong')
print(a9)       #chenxudongshihaoren   a9自身不会变的
a10=a9.partition('dong')
print(a10)        #('chenxu', 'dong', 'shihaoren')成元组
a11=a9.replace('hao','huai')
print(a11)
a12=a9.split('h')
print(a12)              #['c', 'enxudongs', 'i', 'aoren'],h没了,成列表
a13=a9.center(30,'$')
print(a13)       #$$$$$chenxudongshihaoren$$$$$$

a14=a9.find('ri')           #find找不到则返回-1
print(a14)



print('----------列表操作------------')    
a15='xyz'
a7.extend(a15)
print(a7)           #['a', 'b', 'c', 'd', 'x', 'y', 'z']
##a16=a7.find('x')         #列表无find方法
##print(a16)
a16=a7.index('x')        #列表查找元素的位置,只能用index
print(a16)

a17=a7.pop(-2)
print(a17,a7)      #y ['a', 'b', 'c', 'd', 'x', 'z']

a7.sort(reverse=True)
print(a7)



print('----------字典操作------------') 
a18={'a':'aaa','b':123,'c':[1,2,3]}

for i in a18:
    print (i)       #默认打印key
print('-------------')
for i in a18.values():       # 字典名.values()  字典的内置方法
    print(i)
print('-------------')
for i,j in a18.items():       # 字典名.items()  字典的内置方法
    print(i,j)

print('-------------')
      
print(a18.values())      #dict_values(['aaa', 123, [1, 2, 3]])
print(a18.items())#dict_items([('a', 'aaa'), ('b', 123), ('c', [1, 2, 3])])
print(list(a18.items()))  #得到元组的列表[('a', 'aaa'), ('b', 123), ('c', [1, 2, 3])]

a19=a18.get('d',123)
print(a19)

##a20=a18.index("aaa")           字典无index方法
##print(a20)

a21=list(a18.values()).index(123)    # 根据value,得到key.
a22=list(a18.keys())[a21]
print(a21,a22)

a23=a18.popitem()     #移除最后一个键值对,也可移除指定key   a18.pop(key)
print(a23)
print(a18)


#苏州py群给的方法
##the_dict = {'1': 'a', '2': 'b', '3': 'b'}
##the_dict.keys()[the_dict.values().index('b')]
##filter(lambda (x,y): y=='b', the_dict.items())


n1=123
n2=123
print(id(n1),id(n2))      #得到两份相同的地址
n1=66
print(n2)
print(id(n1),id(n2))      #当其中一个修改时,则变为两份地址



print(a18['a'])      #字典的索引要加''


a24=[11,22,33,44,55,66,77,88,99]

print(enumerate(a24))        #<enumerate object at 0x0000000002F9CF78>

a25=dict(enumerate(a24))     #自动生成一列组成字典,默认从0开始
print(a25)


a26=dict.fromkeys(a24,'789')
print(a26)
a27=dict.fromkeys(range(5,11,1),'jjjj')
print(a27)


a28=a24*3       #列表的*法
print(a28)
 
a29=(11,22,33,44,55,66,77,88,99)      #没用了,内存将自动收回
a29=a29[:5]+('aaaaaa',)+a29[5:]     #变相地更改元组
print(a29)        #(11, 22, 33, 44, 55, 'aaaaaa', 66, 77, 88, 99)


a30='abca'
a31=a30.rjust(20,'#')          #右对齐,符串填充
print(a31)                  ##################abc

print(a30.find('a'))      #返回第一个索引位置
print(a30.strip('b'))     #中间的'b'不会去除

print("--------------格式化--------------------")
a32='{0} love {1}'.format('小明','小红')       #位置格式化
print(a32)

a33='{a} hate {b}'.format(a='老鼠',b='猫')     #关键字格式化
print(a33)


print(('%s love %s')%("I",'you'))

print(('%s love %d')%(9,0))    #数字型自动转成字符串--->9 love 0

print('%o'%10)    #格式化无符号的8进制数
print('%x'%160)   #格式化无符号的16进制数(小写)---->a0
print('%X'%160)   #格式化无符号的16进制数(大写)---->A0
print('%f'%(27.678))  #27.678000
print('%e'%23000)    #2.300000e+04
print('%E'%23000)    #2.300000E+04

#m.n    m表示总位数,n表示保留的几位小数
print('%5.3f'%3.142593)   #3.143
print('%15.3d'%3.14159)   #'            003'
print('%+5.3f'%3.142593)   #+3.143         +m 代表前加 + 
print('%#o'%10978)     #0o25342        #代表格式化有符号的不同进制数
print('%010.3f'%78.34567)    #000078.346    0m 代表多余位置用0填充


print('1\n2\"3\'4\a5\n6\t7\\')
'''
1
2"3'45
6	7\
'''
print('1\b2')   #退格符  12
print('1\v2')   #纵向制表符  12
print('1\r2')   #回车符    12
print('1\f2')   #换页符    12
print('1\0a')   #空格符   1 a

print("--------------集合SET--------------------")

set1=set(['a','b','c'])

a34={5,4,3,2,1,1,2,3,4}

print(a34)         #集合的唯一性,{1, 2, 3, 4, 5}

a34.add(9)         #添加元素
a34.remove(4)      #移除元素
print(a34)

a34.pop()          #因为是无序的,故移除随机元素
print(a34)
#del a34[1]
print(a34)

a35=frozenset(set([1,2,3,4,5]))
#a35.add(0)       frozenset,冰冻的,冻结的,不可修改
print(a35)

print("--------------推导式--------------------")

print(type(range(10)))    #<class 'range'>
list1=[i for i in range(10)]   
print(list1)

list2=[i for i in range(10) if i%2==0]
print(list2)

list3=[i*2 for i in range(10)]   
print(list3)


dict1={i:i%2==0 for i in range(10)}
print(dict1)    #{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}

dict1={i:i*2 for i in range(10)}
print(dict1)   #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

#字符串与元组不适用推导式

e=(i for i in range(10))   #e就成了生成器
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))

a36=sum(i for i in range(101) if i%2)
print('100以内的所有奇数相加和为:',a36)








    
