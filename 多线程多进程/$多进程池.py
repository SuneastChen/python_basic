from multiprocessing import Pool



def sum(n):
    s=0
    for i in range(n):
        s+=i
    print(s)  
    

if __name__=='__main__':    #需要加入__name__
    
    n_list=[10000000,20000000,10000000]    #参数列表
    process_list=[]
    p=Pool(processes=3)     #创建了一个有容量的空进程池
    for i in n_list:
        process_list.append(p.apply_async(sum,(i,)))  #进程池生成进程,加入到列表
    # print(process_list)   #是进程对象的列表
    p.close()   #完成后,关闭空进程池

    # for j in process_list:
    #     j.get(timeout=5)    #for循环设置进程的超时等待时间,必须要设,自动执行
    p.join()
    print('主线程结束')