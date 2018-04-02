class People(object):
    address='山东'
    def __init__(self):
        self.name="小明"
        self.age=20

    @classmethod          #类方法定义
    def setNewAddress(cls,add):
        cls.address=add
        


print(People.address)   #类属性,山东

xiaoming=People()

print(xiaoming.address)  #实例属性中没有,找类属性,山东

xiaoming.address='河南'    #增加一个重名的自身属性
print(xiaoming.address)   #自己的属性,河南
print(People.address)    #类属性未更改,还是山东

print('-----------------')
xiaoming.setNewAddress('宿迁')
print(xiaoming.address)      #改了类属性的调用,因为实际对象有了自身的address属性,优于类属性给的,故还是河南

People.setNewAddress('内蒙古')   #调用类方法,更改类属性
print(People.address)   #内蒙古

xiaohong=People()
xiaohong.setNewAddress('江苏')  #实例对象可以调用类方法

print(xiaohong.address)
xiaohong.setNewAddress('昆山')   #当实例对象找不到相应的属性,便会从类属性找,找到然后给实例属性
print(xiaohong.address)


#但类对象不可调用实例属性和实例方法
#实例属性和实例方法依赖于实例对象self


##山东
##山东
##河南
##山东
##-----------------
##河南
##内蒙古
##江苏
##昆山











