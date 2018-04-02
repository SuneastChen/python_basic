#属性:
#cookedLevel 0-3生的,4-5半生不熟的,6-8烤好了,大于8糊了
#cookedString:字符串,描述地瓜的生熟程度
#condiments:配料列表

#方法:
#cook():把地瓜烤一段时间
#addCondiments():给地瓜添加配料
#__init__():默认属性
#__str__():让print对象更好看

class SweetPotato:
    def __init__(self):
        self.cookedLevel=0
        self.cookedString='生的'
        self.condiments=[]

    def __str__(self):
        msg='你的地瓜已经处于'+self.cookedString+'的状态'
        if len(self.condiments)>0:
            msg +=',添加的佐料为:'
            for temp in self.condiments:
                msg=msg+temp+", "
            msg=msg.strip(", ")
        return msg                 #别忘记有返回值
            

    def cook(self,time):
        self.cookedLevel +=time         #通过方法传入更改属性
        if self.cookedLevel>8:
            self.cookedString='烤糊了'
        elif self.cookedLevel>5:
            self.cookedString='熟了'
        elif self.cookedLevel>3:
            self.cookedString='半生不熟'
        else:
            self.cookedString='生的'

    def addCondiments(self,temp):
        self.condiments.append(temp)       #通过方法传入更改属性

digua=SweetPotato()

print("---烤了2分钟---")
digua.cook(2)
print(digua)

print("---又烤了2分钟---")
digua.cook(2)
digua.addCondiments('番茄酱')
print(digua)

print("---又烤了2分钟---")
digua.cook(2)
digua.addCondiments('海鲜酱')
print(digua)

print("---又烤了3分钟---")
digua.cook(3)
print(digua)


#传入time参数,通过方法改变cookedLevel属性,
#根据cookedLevel改变状态属性,然后状态属性被__str__调用

#传入酱料,改变列表属性,然后列表属性的值被__str__调用



##---烤了2分钟---
##你的地瓜已经处于生的的状态
##---又烤了2分钟---
##你的地瓜已经处于半生不熟的状态,添加的佐料为:番茄酱
##---又烤了2分钟---
##你的地瓜已经处于熟了的状态,添加的佐料为:番茄酱, 海鲜酱
##---又烤了3分钟---
##你的地瓜已经处于烤糊了的状态,添加的佐料为:番茄酱, 海鲜酱



















            
            
