print('--------------基本函数操作-----------------')
a34=1234
def test(*a):
    print(len(a))
    print(sum(a))
#    print(a.reverse())       列表.方法不可行
#    print(a34)            不可直接调用全局变量
    
    global a34        #非得调用则加global
    a34=5678          #调用后修改则相当于修改了全局变量
    print(a34)
   
    a35=9999
    b=locals()    #收集局部变量及值,成字典
    print(b) 
       
    
test(1,2,3,4,5,6)
print(a34)          #5678 

#print(a35)         不可直接调用函数内的局部变量
print('-------------函数嵌套与闭包---------------')



##def get():
##        nonlocal a35
##        print(a35)     #不可直接调用父函数变量,除非加入nonlocal
  
def fun1():
    print('我是fun1()')
    def fun2():
        print('我是子函数fun2()')
    fun2()                              #fun1()调用fun2()

fun1()                                #调用

print('-------------return---------------')
def fun3(x):
    def fun4(y):
        return x+y
    return fun4(9)

a1=fun3(3)  
print(a1)



def fun5(x):
    def fun6(y):
        return x+y
    return fun6

a2=fun5(3)       #函数赋给a2了,a2是个函数,<function fun5.<locals>.fun6 at 0x0000000002FE0488>
print(a2)

a3=a2(4)
print(a3)

#就等于以下
a3=fun5(3)(4)    #两次执行,传入两个参数
print(a3)

#当父子函数执行时,可一次执行两次,或先执行一次变成函数赋给一个变量,变量再执行




print('-------------nonlocal---------------')

def fun7():
    a=12
    def fun8():
        nonlocal a
        a*=a
        return a
    fun8()

print(fun7())          #fun7本身无返回值,则返回none

print('-------------return与调用,闭包实现调用父函数变量---------------')
def fun7():
    a=12
    def fun8():
        nonlocal a
        a*=a
        return a
    return fun8

print(fun7())          #返回fun8子函数,fuctionc`



def fun7():
    a=12
    def fun8():
        nonlocal a
        a*=a
        return a
    return fun8()

print(fun7())          #144     即两次返回



def fun7():
    a=12
    def fun8():
        nonlocal a
        a*=a
        return a
    return fun8

print(fun7()())          #144     即两次执行


'''通过子函数的的return,可调用父函数的变量
                        父函数return调用执行子函数,则使用时直接一次执行父函数
                        父函数return子函数名不执行,则使用时父函数需两交执行

'''


print('-------------匿名函数---------------')

g=lambda x,y:x+y
print(g(4,5))

#好处,无需命名,一次调用,精简

print('-------------过滤器,映射---------------')
a4=list(filter(lambda x:x%2,range(4,20,3)))    #过滤器
print(a4)
print(filter(lambda x:x%2,range(4,20,3)))      #得到 filter object


a5=list(map(lambda x:x**2,range(5)))         #映射
print(a5)


print('-------------天才递归,阶乘---------------')

def dgui(n):
    if n==1:
        return 1
    else:
        return n*dgui(n-1)
#a6=int(input('请输入一个正整数:'))     #input得到一个字符串,一定要转成int
a6=10    
a7=dgui(a6)
print('%d的阶乘是:%d'%(a6,a7))
print(a6,'的阶乘是:',a7)   

print('-------------天才递归,斐波拉斯数列第几位的值,从整体到局部的思想---------------')

def fab(n):
    if n<1:
        print('输入有误!')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)


result=fab(10)
print(result)

print('-------------天才递归,汉诺塔---------------')
cs =0
def hanoi(n,x,y,z):
    global cs
    if n==1:
        print(cs,x,'--->',z)
        cs += 1
    else :
        hanoi(n-1,x,z,y)    #将前n-1个盘子从 x--->y
        print(cs,x,'--->',z)   #将最底下的一个从 x--->z
        cs += 1       
        hanoi(n-1,y,x,z)    #将y上的n-1个盘子从 y--->z
#n=int(input('请输入层数:'))        #一定要加入int,转成数字类型
n=3
hanoi(n,'x','y','z')


print('-------------装饰器1---------------')

def fun9():
    return '蛋糕'


def funa(fun):        #装饰器函数
    def funb():        
        return fun()+'+蜡烛!!!'    #子函数可以直接用父函数传进来的参数
    return funb
    
a8=funa(fun9)
print(a8)        #<function funa.
print(a8())      #蛋糕+蜡烛!!!

print('-------------装饰器2---------------')
def fun9():
    return '蛋糕'


def funa(fun):        #装饰器函数
    def funb():
        return fun()+'+蜡烛!!!'
    return funb
    
fun9=funa(fun9)
print(fun9())        #蛋糕+蜡烛!!!.   

print('-------------装饰器3_函数装饰器---------------')

@funa                 #加入@funa
def fun9():
    return '蛋糕'


def funa(fun):        #装饰器函数
    def funb():
        return fun()+'+蜡烛!!!'
    return funb
    
print(fun9())       #蛋糕+蜡烛!!!



print('-------------装饰器4_类装饰器---------------')

class funa(object):
    def __init__(self,fun):
        self.f=fun
    def __call__(self):
        return self.f()+'蜡烛!!!'

@funa                 #加入@funa
def fun9():
    return '蛋糕'

print(fun9())






print('-------------自己改装的装饰器---------------')


def fun9():
    return '蛋糕'


def funa(fun):        #装饰器函数
    
    return fun()+'蜡烛!!!'
    
    
fun9=funa(fun9)    #传入fun9被即时执行
print(fun9)    

'''
@funa 在主函数前加入@装饰器函数名
自己的一级装饰器,无需调用自动执行
二级装饰器(函数嵌套),需调用方可执行

'''
















