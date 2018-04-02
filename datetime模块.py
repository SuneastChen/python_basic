
from datetime import *
#datetime,timedelta,date,time


print('------------------date类方法和属性----------------------')
d1=date(2017,9,30) # date对象
print(d1)      #2017-09-30
print(d1.year)    #2017  其他属性year, month, day
print(d1.replace(year=2018))    #2018-09-30  
#生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
print(d1.timetuple())   #返回日期对应的time.struct_time对象；
#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=273, tm_isdst=-1)
print(d1.weekday())  # 5 返回weekday，如果是星期一，返回0；如果是星期2，返回1
print(d1.isoweekday()) # 6 返回weekday，如果是星期一，返回1；如果是星期2，返回2
print(d1.isocalendar()) #(2017, 39, 6)  返回格式如(year，month，day)的元组；$$$
print(d1.isoformat()) # 返回格式如'YYYY-MM-DD’的字符串；
print(d1.strftime("%Y year %m month %d day"))   #017 year 09 month 30 day   和time模块format相同。

print('------------------date类静态方法和字段----------------------')
import time as time0
print(date.fromtimestamp(time0.time()))   #将时间戳格式化,2017-09-01
print(date.today())    #2017-09-01
# date.max、date.min：date对象所能表示的最大、最小日期；
# date.resolution：date对象表示日期的最小单位。这里是天。


#time类
print('------------------time类静态方法和字段,略----------------------')
print('------------------time类方法和属性----------------------')
t1 = time(10,23,15) #time对象
print(t1)    #10:23:15
print(t1.second)   #15    其他属性t1.hour、t1.minute、t1.second、t1.microsecond：时、分、秒、微秒；
t2=t1.replace(hour=11)
print(t2)    #替换参数创建一个新对象
print(t1.isoformat())   #返回型如"HH:MM:SS"格式的字符串表示;
print(t1.strftime('%H hour %M minute %S second'))  #10 hour 23 minute 15 second  和time模块format相同。




#datetime类
print('------------------datetime类静态方法和字段----------------------')
print(datetime.today())  #返回一个表示当前本地时间的datetime对象；
#2017-09-01 21:13:30.714308
print(datetime.now()) #返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
#2017-09-01 21:13:30.714308
print(datetime.utcnow()) #返回一个当前utc时间的datetime对象；#格林威治时间
print(datetime.fromtimestamp(time0.time())) #根据时间戮创建一个datetime对象，参数tz指定时区信息；
print(datetime.utcfromtimestamp(time0.time()))#根据时间戮创建一个datetime对象；
print(datetime.combine(date(2017,9,1), time(20,30,20))) #根据date和time，创建一个datetime对象；

print('------------------datetime类方法和属性----------------------')
dt=datetime.now()#datetime对象
print(dt.microsecond)   #dt.year、month、day、hour、minute、second、microsecond、tzinfo
print(dt.date())  #获取date对象；
print(dt.time())  #获取time对象；
dt2=dt.replace(year=2020)
print(dt2)     #替换参数创建对象
print(dt.timetuple())  ##返回日期对应的time.struct_time对象；
print(dt.weekday())   
print(dt.isoweekday())   #同上,好用
print(dt.isocalendar())  #(2017, 35, 5) 返回元组$$$
print(dt.isoformat())  #2017-09-01T22:06:28.069565    返回字符串
print(dt.strftime("%Y year %m month %d day %H hour %M minute %S second")) 



print('------------------timedelta类，时间加减----------------------')
#使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法
#class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
#datetime对象的操作包含以下几种：
# datetime2 = datetime1 + timedelta 
# datetime2 = datetime1 - timedelta 
# timedelta = datetime1 - datetime2 
# datetime1 < datetime2
d1=datetime(2017,8,29,8,0,0)
d2=datetime(2017,9,30)      #年,月,日为必须参数,时,分,秒为可选参数
print(d2-d1)       #31 days, 16:00:00
d3 = timedelta(days=35,hours=-4)
print(d1+d3)   #2017-10-03 04:00:00

 


print('------------------tzinfo时区类----------------------')
"""
tzinfo是关于时区信息的类
tzinfo是一个抽象类，所以不能直接被实例化
"""
class UTC(tzinfo):
    """UTC"""
    def __init__(self,offset = 0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)

#北京时间
beijing = datetime.now(UTC(8))
print("beijing time:",beijing)
#曼谷时间
bangkok = datetime.now(UTC(7))
print("bangkok time:",bangkok)
#北京时间转成曼谷时间
print("beijing-time to bangkok-time:",beijing.astimezone(UTC(7)))

#计算时间差时也会考虑时区的问题
timespan = beijing - bangkok
print("时差:",timespan)








