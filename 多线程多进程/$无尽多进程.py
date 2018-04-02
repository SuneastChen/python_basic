from multiprocessing import Process

def sum(n):
    s=0
    for i in range(n):
        s+=i
    print(s)
    

# sum(10000000)
# sum(20000000)
# sum(10000000)
#单进程的单线程需要9.8秒


if __name__=='__main__':    #需要加入__name__
    n_list=[10000000,20000000,10000000]    #参数列表
    for i in n_list:
        p=Process(target=sum,args=(i,))   #args=(n,)其中,必须加上, 传入各参数生成进程
        p.start()   #开始进程
        p.join(0.001)   #挂起,设置阻塞时间,结果是无序
    #----> 需要6.6秒
