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
        

class Horse(Animal):  #直接继承了父类的方法(父类属性和私有方法不会被继承)

#---------------新加入----------------
    horseNum=0

    @classmethod
    def setHorseNum(cls):
        cls.horseNum+=1       #别忘了加cls
        
    def __init__(self,name):    #带有参数的父类方法继承,要改哪个参数,就加入哪个参数,重写
        super().__init__()
        self.name=name
        Horse.setHorseNum()



#---------------新加入----------------



    
    def eat(self):
#        print('我正在吃'+str(self.__a)+'根草')     无法调用,私有属性和方法不会被继承
#但可以通过方法来调用私有属性
        print('我正在吃'+str(self.get__a())+'根草')   #可以调用了私有属性
        

a=Horse('白龙马')

print(a.name)

a.run()

a.eat()

a.set__a(9)
a.eat()

print('-----------------------')

print('共创建了',Horse.horseNum,'匹马儿')
b=Horse('赤兔马')
print('共创建了',Horse.horseNum,'匹马儿')
c=Horse('千里马')
print('共创建了',Horse.horseNum,'匹马儿')

        
print('-------------------------静态方法,类方法实例-------------------------------')
import math 
class Pizza(object):
 def __init__(self, radius, height):
     self.radius = radius
     self.height = height

 @staticmethod
 def compute_circumference(radius):   #静态方法不依赖于实例对象
      return math.pi * (radius ** 2)

 @classmethod
 def compute_volume(cls, height, radius):   #此为形参
      return height * cls.compute_circumference(radius)

 def get_volume(self):
     return self.compute_volume(self.height, self.radius)  #此为实参
#自身的get_volume调用类方法,类方法调用了静态方法,静态方法用到了参数

p=Pizza(5,1)
print(p.get_volume())
print(Pizza.compute_volume(1,5))