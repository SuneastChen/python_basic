print("--------------产生随机数,random--------------------")

import random

for i in range(5):
    a1=random.randint(0,5)      #产生1-5的随机数
    print (a1)


print("--------------OS模块.Operating System--------------------")
#会根据不同的操作系统,调用相应的系统模块
#OS模块中的文件夹的操作
import os

print(os.getcwd())       #得到当前的工作路径
print(os.listdir('.'))     #查看当前工作路径的文件列表 或指定路径  或os.curdir
print(os.listdir('..'))    #查看当前工作路径上一级的文件列表  或os.pardir
 
os.chdir('..')    #改变工作路径
print(os.getcwd()) 


print('----------创建文件夹------------')

os.mkdir("g:\\a")      #创建单层目录文件夹,在上一个目录存在的情况下,文件存在出现异常

#print(os.getcwd())     #不用chdir命令去改变工作路径,则不会变
os.mkdir("g:\\a\\b")    #在a存在怀情况下可以

os.makedirs('g:\\b\\c\\d\\123')  #创建多层路径文件夹,但不能创建文件,文件夹存在出现异常

os.makedirs('g:\\e')     #好用,既可以创建多层目录,又可以创建单层目录



print('----------删除文件夹------------')

#os.remove('g:\\b\\c\\d\\123.txt\\123.txt')   #删除文件

os.rmdir('g:\\a\\b')
os.rmdir('g:\\a')
os.removedirs('g:\\b\\c\\d\\123')  #里面确定是空的,无文件, 则会删除所有空文件夹

os.removedirs('g:\\e')


'''
os.makedirs('g:\\1\\2')

os.rename('g:\\1\\2','g:\\1\\4')    #重命名单层目录
'''
#os.makedirs('g:\\a\\b\\abc')
#os.rename('g:\\a\\b\\abc','g:\\a\\1\\cba')    #不可行,只能重命名最后一个文件夹

print('----------系统命令------------')
#os.system('calc')     
#os.system('cmd')


print(os.name)        #nt
print(os.curdir)      #.
print(os.pardir)      #..
print(os.sep)         #\
print(os.linesep)     #



print("--------------OS.path模块(不属于OS模块)--------------------")

a2=os.path.basename('g:\\a\\b\\abc\\chenxudong.txt')

print(a2)     #chenxudong.txt


a3=os.path.dirname('g:\\a\\b\\abc\\chenxudong.txt')

print(a3)         #???为会么会得到一此乱七八糟的东西  g:\abc 因为是\\
#g:\\a\\b\\abc

a4=os.path.join('g:\\','a','b','abc')
print(a4)       # 将多个字符连起来,成为路径,根目录加g:\\     g:\a\b\abc


a5=os.path.split('g:\\a\\b\\abc\\chenxudong.txt')

print(a5)      #split返回一个元组,存放路径与文件名('g:\\a\\b\\abc', 'chenxudong.txt')

a6=os.path.split('g:\\a\\b\\abc')
print(a6)        #当无文件的路径,则将最后一个文件夹认为是文件('g:\\a\\b', 'abc')


a7=os.path.splitext('g:\\a\\b\\abc\\chenxudong.txt')
print(a7)        #split分离文件名与扩展名,('g:\\a\\b\\abc\\chenxudong', '.txt')

a8=os.path.splitext('g:\\a\\b\\abc')

print(a8)         #无文件名时,('g:\\a\\b\\abc', '')

a9=os.path.getsize ('g:\\123.txt')
print(a9)      #返回文件大小单位,字节

a10=os.path.getatime ('g:\\123.txt') #access 读取,进入
a11=os.path.getctime ('g:\\123.txt') #create 创建
a12=os.path.getmtime ('g:\\123.txt') #modification 修改
print(a10,'\n',a11,'\n',a12)

import time
a10_1=time.localtime(a10)
print(a10_1)  #time.struct_time(tm_year=2017, tm_mon=7, tm_mday=6, tm_hour=23,tm_min=31, tm_sec=35, tm_wday=3, tm_yday=187, tm_isdst=0)
    

#返回为True/False函数

a13=os.path.isdir('g:\\会计\\CPA')

print(a13)     #路径是否存在且是一个路径

a13=os.path.isdir('g:\\123.txt')
print(a13)     #false



a14=os.path.isfile('g:\\123.txt')
print(a14)      #路径是否存在,且是一个文件


a15=os.path.exists('g:\\会计\CPA')

print(a15)       #路径是否存在

a16=os.path.isabs('g:\\会计\CPA')

print(a16)    #是否是绝对路径

print('------------------------')

#是否是一个链接,有问题都返回False ???
a17=os.path.islink('g:\\会计\\CPA\\123.txt')
print(a17)

a18=os.path.islink('g:\\会计\\CPA\\456.txt')
print(a18)

a19=os.path.islink('g:\\会计\\CPA')
print(a19)


a20=os.path.ismount('g:\\会计\\CPA')
print(a20)         #是否是一个根目录,磁盘目录
a21=os.path.ismount('g:\\')
print(a21)



a22=os.path.samefile('g:\\会计\\CPA','g:\\会计\\CPA')
print(a22)       #两个路径是否指相同的文件



print("--------------模块知识--------------------")

import sys
print(sys.path)   #查看安装模块的路径

print("--------------time模块--------------------")

import time
print(time.time())    #第一种时间戳 1500200868.412479

print(time.gmtime())
print(time.localtime())
# 第二种元组 time.struct_time(tm_year=2017, tm_mon=7, tm_mday=16, tm_hour=10, tm_min=16, tm_sec=20, tm_wday=6, tm_yday=197, tm_isdst=0)

print(time.ctime())    #第三种格式化的时间 Sun Jul 16 18:30:22 2017    或者1转3
print("--------------时间格式转换--------------------")
print(time.asctime(time.localtime()))  # 2转换成3 Sun Jul 16 18:33:03 2017
print(time.asctime())   #未传参数时,默认传入本地时间

print(time.mktime(time.gmtime()))   #2转成1    1500178946.0


print(time.strftime("%Y-%m-%d %X"))   #2017-07-16 21:03:25
print(time.strftime("%x  %X"))       # 07/16/17  21:03:25
print(time.strftime("%c"))    #07/16/17 21:17:22 本地的完整时间显示
print(time.strftime("%B"))    #July  本地完整的月份显示
print(time.strftime("%A"))   #Sunday 本地完整的星期显示


print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))   #变成元组







# print(time.daylight(45))
	
time.sleep(1)   #延迟1移再执行

print("--------------系统运行时间-------------------")

print(time.clock())   #返回cpu的运行时间,用来衡量不时程序的耗时

time.sleep(1)  
print( "clock1:%s" % time.clock())   #第一个clock()输出的是程序运行时间
time.sleep(1)  
print ("clock2:%s" % time.clock())   #第二、三个clock()输出的都是与第一个clock的时间间隔
time.sleep(1)  
print ("clock3:%s" % time.clock())
#clock()   在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间



print(time.process_time())     #返回进程的运行时间,纯粹的运行时间
print(time.perf_counter())     #返回系统的运行时间,一共运行了多久,包括等待时间
time.sleep(1) 
print(time.process_time())     #返回进程的运行时间
print(time.perf_counter())     #返回系统的运行时间,一共运行了多久,包括等待时间












