# _*_ coding:utf-8 _*_
#!/usr/bin/python34


print("-----------------自定义迭代器------------------")

a12='人生就是生命的体验!'
for i in a12:        #内部自动调用__iter__()和__next__()方法
    print(i)

#实现与迭代器相同功能的代码
a12=iter(a12)   #1.先把a12放在迭代器中
while 1:          #2.可以用next()
    try:
        i=next(a12)
        print(i)
    except StopIteration:     #迭代完了产生StopIteration异常
        break


print("-----------------迭代器的魔法方法(用于类定义),生成斐波拉斯序列------------------")
class Fibs:
    def __init__(self,n=300):
        self.a=0
        self.b=1
        self.n=n
    def __iter__(self):
        return self       #__iter__返回self
    def __next__(self):   #自定义next()的方法
        self.a,self.b=self.b,self.a+self.b
        if self.a>self.n:
            raise StopIteration
        return self.a

f=Fibs(100)
for i in f:        #for语句自动调用__iter__()和__next__()方法,不占用内存,有可重用的返回值
    print(i)

print("-----------------生成器(用于函数定义,是特殊的迭代器),yield(相当于return),但可挂起,暂停------------------")
def myGen():
    print('我是生成器,被执行了!')
    yield 1
    yield 2
    yield 3             #带有 yield 的函数在 Python 中被称之为 generator生成器
print(myGen())    #<generator object myGen at 0x0000000002907630>
#错误的执行方式:
print(next(myGen()))
print(next(myGen()))
print(next(myGen()))
#以下执行了三次,不可这样写
# 我是生成器,被执行了!
# 1

#正确的执行方法:
myg=myGen()       #先赋给一个变量,不会执行任何代码
print(next(myg))
print(next(myg))
print(next(myg))
#print(next(myg))

# 我是生成器,被执行了!
# 1
# 2
# 3
#StopIteration

print("-----------------打印出100以内的能被3整除的正整数--------------------")

#写法1:迭代器写法
for i in range(101):
    if i %13==0:
        print(i)

print('-----------------')
#写法2:生成器写法
def one():
    i = 0
    while 1 :
        i += 1
        if i % 13==0:
            yield i


for j in one():  #one()就相当于能被13整除的无限数列
    if j<101:
        print(j)
    else:break
    


print("-----------------生成器函数同样可以传入参数--------------------")
def counter(start=0):
    while True:
        yield start
        start += 1

for i in counter(9):
    if i >15:
        break
    print(i)




print("-----------------生成器(用于函数定义),生成斐波拉斯序列--------------------")

def libs():
    a=0
    b=1
    yield a
    yield b
    while 1:
        a,b=b,a+b
        yield a     #被next()或for语句调用所返回的值

for num in libs():
    if num>100:       #如果需要有个范围,加个if语句
        break
    print(num,end=' ')

#[0 1] 1 1 2 3 5 8 13 21 34 55 89


print('\n')

print("-----------------生成器函数与finally-----------")
def play_u():
    try:
         yield 1
         yield 2
         yield 3
    finally:
        yield 0

for val in play_u(): print(val)
#1,2,3,0      暂停了,并没有离开函数本身,finally不会执行





#以下语法错误不可以这样写,生成器与迭代器,不可再用yield返回
# for i in play_u():
#     yield i
  
# for i in range(5):
#     yield i





#生成器用于读文件函数实例
'''
def read_file(fpath): 
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
             if block: 
                   yield block 
            else: 
                 break

'''

print("-----------------迭代器与推导式-----------")

#假如用元组推导式:
e=(i for i in range(10))   #e就成了生成器
print(type(e))    #<class 'generator'>
print(next(e))
print(next(e))
print(next(e))
print(next(e))
#print(e.next())    不可这样写   AttributeError: 'generator' object has no attribute 'next'
#列表,字典推导式
list1=[i for i in range(10)]
list2=[i for i in range(10) if i%2==0]
dict1={i:i*2 for i in range(10)}




print("----------------------协同程序-----------------------")

def repeater():
    n=0
    print('我是循环之前语句')
    while True:
        n = yield n*2
        print('我是yield之后的语句正在执行')

r = repeater()    #r为生成器函数,此句不会执行任何代码
print(next(r))  #预执行生成器函数,先要开启生成器,不会执行print('我是yield之后的语句正在执行')
#---->>'我是循环之前语句'
#---->> 0
print(r.send(10))    #先接收n=10,再往下执行代码,直到执行yield n*2
#print('我是yield之后的语句正在执行')
#---->> 20





print("-------查找ben-------")

def get_result(content):
    print('开始查找%s\n'% content)
    while 1:
        line=yield
        print('我是yield之后的语句')
        if content in line:
            print(line)

result=get_result('ben')  #此句指定生成器函数,不会执行任何代码

next(result)   #预执行,生成器函数(返回'',),让其开启,相当于发动机已经开启
#--->>开始查找ben
#--->>''
result.send('i love ben')     #line='i love ben' ,往下执行,直到yield
# --->>我是yield之后的语句
#--->>'i love ben'
result.send('my name is ben')
# --->>我是yield之后的语句
#--->>'my name is ben'
result.send('tom is good boy')
# --->>我是yield之后的语句
result.close()     #用完关闭生成器





