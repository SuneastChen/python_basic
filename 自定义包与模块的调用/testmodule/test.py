print('-------------return与调用,闭包实现调用父函数变量---------------')

def fun7():
    a=12
    def fun8():
        nonlocal a
        a*=a
        return a
    return fun8


'''通过子函数的的return,可调用父函数的变量
                        父函数return调用执行子函数,则使用时直接一次执行父函数
                        父函数return子函数名不执行,则使用时父函数需两交执行

'''

if __name__=='__main__':   #自己用时,__name__返回__main__,执行以下语句

    print(fun7()())          #144     即两次执行