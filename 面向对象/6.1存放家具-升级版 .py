class Home:
    def __init__(self,area):
        self.area=area
        self.rongNaList=[]
        self.light='off'           #加入灯属性

    def __str__(self):
        msg='家当前可用面积为:'+str(self.area)+';灯的状态为:'+self.light

        if len(self.rongNaList)>0:      #加入当前物品显示
            msg +=';当前物品有:'
        
            for temp in self.rongNaList:
                msg += temp.getBedName()+', '
                msg=msg.strip(', ')
        return msg
    
    def containItem(self,item):        #item传入的参数为床对象
        bedArea=item.getBedArea()       #用方法获取床对象的属性,bedArea只是函数中的局部变量,不是类属性,外部不可使用
        

        if self.area>bedArea:
            self.rongNaList.append(item)   #将item对象加入列表
            self.area-=bedArea
            print('当前添加%s成功...家当前可用面积为:%d'%(item.getBedName(),self.area))
        else:
            print('添加不成功!当前%s的面积大于家的可用面积'%(item.getBedName()))

    def turnOn(self):
        self.light='on'

        for temp in self.rongNaList:
            temp.setLight()           #只有加入列表的物品才会修改属性,超级3p大床未加入,故其明暗状态仍然是默认的off

    def turnOff(self):
        self.light='off'

        for temp in self.rongNaList:
            temp.setLightOff()
        
    

class Bed:
    def __init__(self,name,area):
        self.area=area
        self.name=name
        self.light='off'

    def __str__(self):
        msg=self.name+'占用的面积为:'+str(self.area)+';'+self.name+'的明暗状态为:'+self.light
        return msg

    def getBedArea(self):
        return self.area

    def getBedName(self):
        return self.name

    def setLight(self):
        self.light='on'

    def setLightOff(self):
        self.light='off'
        
    

home=Home(180)
print(home)

bed1=Bed('席梦思床',10)
print(bed1)
home.containItem(bed1)
print(home)
print('------------------------')


bed2=Bed('弹簧床',20)

home.containItem(bed2)
print('开灯')
home.turnOn()
print(bed1)
print(bed2)
print(home)
print('------------------------')


bed3=Bed('超级3p大床',200)
home.containItem(bed3)
print('关灯')
home.turnOff()
print(home)
print(bed1)
print(bed2)
print(bed3)

print('------------------------')

print('开灯')
home.turnOn()
print(home)
print(bed1)
print(bed2)
print(bed3)


print(id(bed1))
print(id(bed2))



##家当前可用面积为:180;灯的状态为:off
##席梦思床占用的面积为:10;席梦思床的明暗状态为:off
##当前添加席梦思床成功...家当前可用面积为:170
##家当前可用面积为:170;灯的状态为:off;当前物品有:席梦思床
##------------------------
##当前添加弹簧床成功...家当前可用面积为:150
##开灯
##席梦思床占用的面积为:10;席梦思床的明暗状态为:on
##弹簧床占用的面积为:20;弹簧床的明暗状态为:on
##家当前可用面积为:150;灯的状态为:on;当前物品有:席梦思床弹簧床
##------------------------
##添加不成功!当前超级3p大床的面积大于家的可用面积
##关灯
##家当前可用面积为:150;灯的状态为:off;当前物品有:席梦思床弹簧床
##席梦思床占用的面积为:10;席梦思床的明暗状态为:off
##弹簧床占用的面积为:20;弹簧床的明暗状态为:off
##超级3p大床占用的面积为:200;超级3p大床的明暗状态为:off
##------------------------
##开灯
##家当前可用面积为:150;灯的状态为:on;当前物品有:席梦思床弹簧床
##席梦思床占用的面积为:10;席梦思床的明暗状态为:on
##弹簧床占用的面积为:20;弹簧床的明暗状态为:on
##超级3p大床占用的面积为:200;超级3p大床的明暗状态为:off
##46579496
##46579608



