class Animal(object):
    def __init__(self,name='动物',color='白色',type1='哺乳类'):
        self.name=name
        self.color=color
        self.type1=type1
        self.__a=4       #私有属性

    def run(self):
     
        print('我在吃了'+str(self.__a)+'根草')   #私有属性只能在类定义中调用
        print('我在不断地奔跑...')


    def get__a(self):
        return self.__a

    def set__a(self,nub):
        self.__a=nub
        

class Horse(Animal):  #直接继承了父类的方法(除私有属性和私有方法)


    def run(self):   #重写父类方法
        super().run()         #加载父类方法
        print('而且是边唱边跳地奔跑...')


    def eat(self):
#        print('我正在吃'+str(self.__a)+'根草')     无法调用,私有属性和方法不会被继承
#但可以通过方法来调用私有属性
        print('我正在吃'+str(self.get__a())+'根草')   #可以调用了私有属性
        

a=Horse('马')

print(a.name)
print('--------------')
a.run()
print('--------------')
a.eat()

a.set__a(9)
a.eat()

##马
##--------------
##我在吃了4根草
##我在不断地奔跑...
##而且是边唱边跳地奔跑...
##--------------
##我正在吃4根草
##我正在吃9根草



class Dog:
    def __init__(self,a):
        self.name=a
    def __del__(self):
        print('我'+self.name+'已经死了')

aa=Dog('汪财')
print('-----------')
del aa


print('-----------------------钻石继承,菱形继承问题------------------------')

class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")

d = D()
# 进入D…
# 进入B…
# 进入A…
# 离开A…
# 离开B…
# 进入C…
# 进入A…
# 离开A…
# 离开C…
# 离开D…
#问题点进入A两次了



print('-----------------钻石继承,菱形继承问题解决,super().__init__()------------------')

class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")

d = D()
# 进入D…
# 进入B…
# 进入C…
# 进入A…
# 离开A…
# 离开C…
# 离开B…
# 离开D…


print('------------------继承的传参问题-----------------')

class A:
    def __init__(self,a1,a2,a3=100):    #父类有个默认参数,
        self.a1=a1
        self.a2=a2
        self.a3=a3

class B(A):
    def __init__(self,b,a1,a2,a3=300):   #子类有个默认参数
        super().__init__(a1,a2,a3=200)   
        #调用父类方法(传入的是实参),父类占用了一些参数,此处父类与子类的形参需相同,无顺序
        self.b=b
b=B(1,2,3,4)
print(b.a1)
print(b.a2)
print(b.a3)   #最后a3为200,因为200是实参,100与300都是默认参数
print(b.b)


