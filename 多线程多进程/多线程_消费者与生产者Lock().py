import random
import time
import threading

MONEY = 0
gLock=threading.Lock()

def procuder():
    while 1:
        global MONEY
        time.sleep(1)
        random_money=random.randint(10,100)
        
        gLock.acquire()   #用全局变量之前,加锁
        MONEY += random_money
        gLock.release()   #用完之后,释放锁

        print('本线程%s生产了%d,总额为%d' % (threading.current_thread,random_money,MONEY))
        #print(threading.activeCount())

def customer():
    while 1:
        global MONEY
        random_money=random.randint(10,100)
        time.sleep(1)
        if MONEY > random_money:

            gLock.acquire()   #用全局变量之前,加锁
            MONEY -= random_money
            gLock.release()   #用完之后,释放锁

            print('本线程%s消费了%d,余额为%d' % (threading.current_thread,random_money,MONEY))
        else:
            print('本线程%s需要消费%d,余额为%d,余额不足!' % (threading.current_thread,random_money,MONEY))
        

def test():
    #执行三个线程来当作生产者
    for x in range(3):
        th=threading.Thread(target=procuder)
        th.start()
    #执行三个线程来当作消费者
    for x in range(3):
        th=threading.Thread(target=customer)
        th.start()

if __name__ == '__main__':
    test()
    print('主线程结束')
    #不用Lock()的话,会在短的运行时间内给MONEY,造成混乱