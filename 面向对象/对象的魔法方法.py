print("------------------调用模块------------------")
# import testmodule
# a=testmodule.test.fun7()()   不可行
# print(a)

from testmodule import test as t
a=t.fun7()()
print(a)

print("------------------对象的函数------------------")
class Animal(object):
    """docstring for Animal"""
    def __init__(self, color="白色"):
        self.color = color


class Dog(Animal):
    """docstring for Dog"""
    def __init__(self):
        super(Dog, self).__init__()
        
aa=Dog()

print(issubclass(Dog,Animal))    #第一个类是第二个类的子类,True

print(isinstance(aa,Animal))     #检查一个实例对象是否属于指定的类
print(isinstance(aa,Dog))        #父类与子类均返回True,若第一个参数不是实例对象,则False
                                                      # 若第二个参数不是类/类元组,则TypeError
print(hasattr(aa,'color'))                                                      
print(getattr(aa,'color'))
print(getattr(aa,'height','没有哦,这个属性'))
setattr(aa,'name','旺财狗')
print(getattr(aa,'name'))
delattr(aa,'name')
print(getattr(aa,'name','无此属性'))

print(dir(aa))    #查看对象的所有内置方法

print("------------------魔法方法,构造__init__,__new__------------------")
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #不可有return
    def getPeri(self):
        return (self.x+self.y)*2
    def getArea(self):
        return self.x*self.y

a=Rectangle(4,5)
print(a.getPeri())
print(a.getArea())



class CapStr(str):
    def __new__(cls,zifu):   #重写父类方法,定义时的传参
        zifu=zifu.upper()
        return str.__new__(cls,zifu)
b=CapStr('i love you!')    #使用时的传参
print(type(b))    #<class '__main__.CapStr'>
print(b)
print("------------------魔法方法,析构__del__------------------")

class C:
    def __init__(self):
        print('我是init方法,被调用了...')
    def __del__(self):
        print("我是__del__方法,我被调用了...")      #程序运行完调用,或不再引用了
c1=C()
c2=C()

del c1

print("------------------魔法方法,算术运算------------------")

print(type(len))     #<class 'builtin_function_or_method'>
print(type(dir))     #<class 'builtin_function_or_method'>
print(type(int))     #<class 'type'>
print(type(list))    #<class 'type'>

class X():
    pass
x=X()
print(type(X))      #<class 'type'>
print(type(x))      #<class '__main__.X'>    type(x)==X
print(X)           #<class '__main__.X'>
print(x)          #<__main__.X object at 0x0000000002762470>


print(divmod(5,3))    #(1, 2)    返回一个元组(5//3,5%3)

a1=int("123")      #实例化对象a1
a2=int("456")     #实例化对象a2
print(a1+a2)       #实例化对象的加法

#自定义加减法
class New_int(int):     #继承
    def __add__(self,other):    #重写父类方法
        return int.__sub__(self,other)   #父类名.父类方法调用
    def __sub__(self,other):
        return int.__add__(self,other)

a3=New_int("3")
a4=New_int("4")
print(a3+a4)
print(a3-a4)

#不可行的方法,会无限递归
# class Try_int(int):
#     def __add__(self,other):
#         return self+other
#     def __sub__(self,other):
#         return self-other

class Try_int(int):
    def __add__(self,other):
        return int(self)+int(other)    #转换成整型后进行运算
    def __sub__(self,other):
        return int(self)-int(other)
a5=Try_int('5')
a6=Try_int('6')
print(a5+a6)
print(a5-a6)

print("------------------魔法方法,算术运算---反运算------------------")

class Nint(int):
    def __rsub__(self,other):
        return int.__sub__(self,other)

a7=Nint('7')
print(3-a7)     #得到-4,因为当实例对象有方法时,会先调用实例对象的方法



a8=8
a9=9
a10=complex(a8,a9)
print(a10)     #(8+9j) 求复数  可以自定义方法__complex__(self)

print(type(a10))



print("------------------定制方法,时间实例------------------")

import time as t

class MyTimer():
    def __init__(self):
        self.unit=['年','月','日','时','分','秒']
        self.prompt='未开始记时'
        self.lasted=[]
        self.begin=0
        self.end=0
    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __add__(self,other):    #定义两个对象相加的方法,传入两个对象
        prompt='总共运行了'     #局部变量
        result=[]
        for x in xrange(6):
            result.append(self.lasted[x]+other.lasted[x])
            if result[x]:
                prompt+=(str(result[x])+self.unit[index])
        return prompt
        

    def start(self):
        self.begin=t.localtime()
        self.prompt='请先调用stop()停止计时!'
        print('计时开始...')
    def stop(self):
        if self.begin==0:
            print("请先调用start()开始计时!")
        else:
            self.end=t.localtime()
            self.__calc()               #调用私有方法
            print('计时结束!')
    def __calc(self):
        self.lasted=[]
        self.prompt='总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index] !=0:
                self.prompt+=str(self.lasted[index])+self.unit[index]
        #为下一轮计时初始化设置
        self.begin=0
        self.end=0




t1=MyTimer()
t1.stop()
t1.start()
t.sleep(2)
print(t1)
t1.stop()
print(t1)














print("------------------对象属性的魔法方法------------------")


class C(object):
    def __getattribute__(self,name):     #对象被访问时的行为,包括不存在属性时
        print("我在调用__getattribute__")
        return super().__getattribute__(name)  #写的与父类相同的方法,只是加个print
    def __getattr__(self,name):     #访问属性不存在时的行为,需要自定义
    #从对象中读取某个属性时，首先需要从self.__dict__中搜索该属性，再从__getattr__中查找
        print('我在调用__getattr__')
        return '这个属性不存在'
    def __setattr__(self,name,value):    #只有__setattr__有value参数
        print("我正在调用__setattr__")
        return super().__setattr__(name,value)
    def __delattr__(self,name):
        print("我正在调用__delattr__")
        return super().__delattr__(name)


c=C()
print(c.x)    #我在调用__getattribute__     我在调用__getattr__   这个属性不存在

c.x=2       #我正在调用__setattr__
print(c.x)   #我在调用__getattribute__     2

del c.x      #我正在调用__delattr__

print("-----------------正方形实例------------------")
class Rectangle(object):
    def __init__(self, width=0,height=0):
        self.width=width
        self.height=height

    def __setattr__(self,name,value):
        if name=="square":        #如果属性名=="square"
            self.width=value
            self.height=value
        else:
            # self.width=width       会陷入死循环!!!!!
            # self.height=height
            # 
            super().__setattr__(name,value)   #否则调用内部的魔法方法,自动设置,推荐使用
            #或者self.__dict__[name]=value    实例对象.__dict__ 查看对象的所有属性的字典,加入字典中也可行

    def get_area(self):
        return self.width*self.height

r1=Rectangle(4,5)
print(r1.get_area())

r1.square=10
print(r1.width)
print(r1.height)
print(r1.get_area())

print(r1.__dict__)   #得到所有属性的健值对成字典 {'width': 10, 'height': 10}

        
print("-----------------描述符------------------")
    
class My_decriptor(object):    #定义描述符类
    def __get__(self,instance,owner):        #self,instance,owner三个参数
        print("getting",self,instance,owner)   #My_decriptor,test(实例对象),Test
    def __set__(self,instance,value):
        print("setting",self,instance,value)   #My_decriptor,test(实例对象),123
    def __delete__(self,instance):
        print("deleting",self,instance)  #My_decriptor,test(实例对象)
class Test(object):
    x=My_decriptor()     #描述符就是将特殊的类,指派给另一个类的属性,此属性设置,获取,删除调用相应的行为

test=Test()  
print(test.x) #getting  My_decriptor,test(实例对象),Test
test.x=123    #setting  My_decriptor,test(实例对象),123
print(test.x) #并不会得到123!!!!!,而是getting  My_decriptor,test(实例对象),Test
del test.x    #deleting My_decriptor,test(实例对象)

print("-----------------自定义Property------------------")
class My_property(object):
    def __init__(self, fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        return self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)

class C(object):
    
    def __init__(self):
        self.__x = None
    def getX(self):
        return self.__x
    def setX(self,value):
        self.__x=value
    def delX(self):
        del self.__x
    x=My_property(getX,setX,delX)    #通过描述符,实现在描述符中调用自己的getX,setX,delX
c=C()
c.__x=123

print(c.__x)

del c.__x
print(help(c))

print("-----------------自带的Property用法1------------------")

class Test(object):
    def __init__(self):
        self.__value=None
    def get(self):        
        return self.__value
    def set(self,value):
        print("正在调用set方法")
        self.__value=value
    x=property(get,set)    #此句才时property的关键

t=Test()
print(t.x)
t.x=999
print(t.x)               #通过x访问和设置Test的私有属性__value

print("-----------------自带的Property用法2------------------")
class Student(object):
    @property             #定义__get__方法
    def score(self):
        return self._score
 
    @score.setter          #定义__set__方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score)  ## OK，实际转化为s.get_score()

#s.score = 9999  #raise ValueError('score must between 0 ~ 100!')
#该属性不是直接暴露的，而是通过getter和setter方法来实现的






print("-----------------温度转换实例------------------")
        
class Celsius:
    def __init__(self,value=26):
        self.value=float(value)
    def  __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)

class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel*1.8+32
    def __set__(self,instance,value):
        instance.cel=(float(value)-32)/1.8
class Temperature:
    cel=Celsius()
    fah=Fahrenheit()

temp=Temperature()
print(temp.cel)
print(temp.fah)

temp.cel=30
print(temp.fah)

temp.fah=100
print(temp.cel)   
# 此句执行的顺序:
# temp.fah=100
# instance.cel=(float(value)-32)/1.8
# cel=Celsius()        
# self.value=float(value)

print("-----------------自定义列表,返回访问元素的次数,__getitem__(self,key)------------------")
class CountList():
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]

a11=CountList(0,11,22,33,44,55)
print(a11[1])
print(a11[1]+a11[5])
print(a11.count)

