import random

class Sprite:  #定义精灵类
    
    step=[-2,+2,-3,+3]

    def __init__(self,gm,point=None):   #传入gm对象,以便使用gm的方法
        self.gm=gm
        if point is None:
            self.point=random.randint(0,20)
        else:
            self.point=point

    def jump(self):
        astep=random.choice(Sprite.step)  #astep是函数的局部变量,不是一个类属性
        if 0<=self.point+astep<=20:
            self.point += astep


class Ant(Sprite):

    def __init__(self,gm,point=None):
        super().__init__(gm,point)
        self.gm.set_point('ant',self.point)

    def jump(self):
        super().jump()
        self.gm.set_point('ant',self.point)    #此句是本游戏的核心,将gm实例对象作为属性,调用gm的方法,传入新参数


class Worm(Sprite):

    def __init__(self,gm,point=None):
        super().__init__(gm,point)
        self.gm.set_point('worm',self.point)

    def jump(self):
        super().jump()
        self.gm.set_point('worm',self.point)


class GameMap:
    def __init__(self):
        self.ant_point=None
        self.worm_point=None

    def catched(self):
        print('ant:',self.ant_point,'worm:',self.worm_point)
        if self.ant_point is not None and self.worm_point is not None and self.ant_point == self.worm_point:
            return True

    def set_point(self,src,point):
        if src =='ant':
            self.ant_point=point      #传入新参数,改变map属性,然后进入判断循环
        if src == 'worm':
            self.worm_point=point

if __name__ == '__main__':    #__main__
    gm=GameMap()
    worm=Worm(gm)
    ant=Ant(gm)
    while not gm.catched():
        worm.jump()
        ant.jump()
    

#初始point,跳得到新point,新point传入map,更新map属性point,然后判断打印point,
          #进入循环跳,判断








        
        
    
    
    
