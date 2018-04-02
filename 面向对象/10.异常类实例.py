
print('------------------自定义异常类------------------------')
class ShortException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)    #或者 super().__init__()
        self.length=length
        self.atleast=atleast



try:
    #s=input('请输入--->')
    s="123"
    changd=5

    if len(s)<changd:
        raise ShortException(len(s),changd)   #产生异常,传入参数

except ShortException as x:     #x这个变量绑定到了错误实例
    print('ShortException错误产生,您输入的长度为%d,\
长度至少为%d'%(x.length,x.atleast))

else:   #没有异常时执行的代码
    print('good!没有异常发生')
    
print('------------------一般异常------------------------')

try:
    f=open('g:\\345.txt')
    print(f.read())
    f.close()
except OSError as j:
    print('出错啦!原因是:'+str(j))

print('------------------自爆异常------------------------')
raise TypeError('数据类型异常了哦,你再检查一下吧!')  #系统报自己的错












