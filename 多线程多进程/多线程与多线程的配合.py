import time
import threading

def ten():
    global lock,start_list,mid_list
    #必须要大于等于线程数,子线程正常运行生产,后面还有9个线程正在运行尚未完成
    while len(start_list)>=10:
        time.sleep(2)    
        lock.acquire()
        num = start_list.pop(0) *10        
        mid_list.append(num)
        lock.release()
        print(num)

def five():
    global lock,mid_list,result_list
    while 1:
        # mid_list个数>=线程数 ---> 当前待加式产品量大,流水线正常生产
        if len(mid_list)>=10:
            time.sleep(3)
            lock.acquire()
            num = mid_list.pop(0) + 5
            result_list.append(num)
            lock.release()
            print(num)
        # 虽然当前任务不多,但只要上一个车间有在生产运作,就不能关闭流水线   
        elif threading.activeCount()>11:
            continue
        # 当前作务不足,且上一车间的流水线都关闭了,就可以关闭当前的流水线了
        else:
            break

start_list = [i for i in range(30)]  # 原材料仓库
mid_list =[]  # 中间周转仓库
result_list = []  # 成品仓库
lock = threading.Lock()  # 仓库的锁
mythread=[]  # 老板的记事本,让老板有责任心

for i in range(10):  # 老板造车间1的流水线,并开启
    t = threading.Thread(target=ten)
    t.start()
  
for i in range(10):  # 老板造车间2的流水线,并开启,记录到老板记事本中
    t = threading.Thread(target=five)
    # 设置流水线重不重要,老板把自己的事干完了,需不需要老板等待,默认重要,需要等待
    # t.setDaemon(0)
    t.start()
    mythread.append(t)
    
# 将主线程阻塞等待,老板需要等待车间的流水线结束,才干能自己的事
# 如果不加的话,是一位责任心不强的老板,先把自己的事干完了,再等待流水线结束
for i in range(10):  
    mythread[i].join()

print(result_list)
print('*'*20,'主线程结束')