# _*_ coding:utf-8 _*_
#!/usr/bin/python36



from asyncio import iscoroutinefunction
from types  import coroutine
async def one():      #定义协程函数
    print('函数1开始')
    await get_change()
    print('函数1结束')



async def two():
    print('函数2开始')
    print('函数2:python')
    await get_change()
    print('函数2:golang')
    print('函数2:java')
    print('函数2结束')

@coroutine     #用了 from types  import coroutine 模块
def get_change():
    yield

one=one()
two=two()


for i in range(2):
    try:
        one.send(None)
    except StopIteration as e:
        print('one函数结束异常 ')

    try:
        two.send(None)
    except StopIteration as e:
        print('two函数结束异常了')










