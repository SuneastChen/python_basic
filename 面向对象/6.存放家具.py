class Home:
    def __init__(self,area):
        self.area=area
        self.rongNaList=[]

    def __str__(self):
        msg='家当前可用面积为:'+str(self.area)
        return msg
    
    def containItem(self,item):        #item传入的参数为床对象
        bedArea=item.getBedArea()       #用方法获取床对象的属性,bedArea只是函数中的局部变量,不是类属性,外部不可使用
        

        if self.area>bedArea:
            self.rongNaList.append(item)
            self.area-=bedArea
            print('当前添加%s成功...家当前可用面积为:%d'%(item.getBedName(),self.area))
        else:
            print('添加不成功!当前%s的面积大于家的可用面积'%(item.getBedName()))
    

class Bed:
    def __init__(self,name,area):
        self.area=area
        self.name=name

    def __str__(self):
        msg=self.name+'占用的面积为:'+str(self.area)
        return msg

    def getBedArea(self):
        return self.area

    def getBedName(self):
        return self.name
    

home=Home(180)
print(home)

bed1=Bed('席梦思床',10)
print(bed1)
home.containItem(bed1)
print(home)

bed2=Bed('弹簧床',20)
home.containItem(bed2)
print(home)

bed3=Bed('超级3p大床',200)
home.containItem(bed3)
print(home)


##家当前可用面积为:180
##席梦思床占用的面积为:10
##当前添加席梦思床成功...家当前可用面积为:170
##家当前可用面积为:170
##当前添加弹簧床成功...家当前可用面积为:150
##家当前可用面积为:150
##添加不成功!当前超级3p大床的面积大于家的可用面积
##家当前可用面积为:150











