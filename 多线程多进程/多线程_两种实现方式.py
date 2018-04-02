
import threading
import time

'''
def say(n):
    time.sleep(5)
    print(n,'次,hello world!')


#直接用单线程执行三次
# say(1)
# say(2)
# say(3)
#单线程执行三次需要15秒


#多线程方法一:-------创建线程对象
n_list=[1,2,3,4,5,6,7,8,9]   #参数列表
mythread=[]

for i in n_list:     
    t=threading.Thread(target=say,args=(i,))
    t.start()   #各线程开始
    # t.join(0.01)   #子线程阻塞时间,同时主线程也阻塞了; 若不传参,则子线程挂起,直到运行结束,再往下执行
    #mythread.append(t)   #将线程对象 加入线程列表,也可不加
#print(mythread)    #mythread是线程的列表
#------>> 多线程执行三次只需要5.5秒
print('我是主线程')

'''
#多线程方法2:-------创建多线程类(继承threading.Thread)
class Mythread(threading.Thread):
    def __init__(self,args):
        threading.Thread.__init__(self)
        self.args=args
    def run(self):      #重写run方法,即把处理的函数搞进去
        time.sleep(5)
        print(self.args,'次,hello world!')

n_list=[1,2,3,4,5,6,7,8,9]   #参数列表
for i in n_list:
    t=Mythread(i)   #创建自定义类的实例对象
    t.start()



