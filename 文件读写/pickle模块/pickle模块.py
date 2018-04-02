# _*_ coding:utf-8 _*_
#!/usr/bin/python34
print('-------------------pickle写入,读取文件4--------------------')


import pickle

b2=[99,88,77,'我爱你','世界!']

f=open('my_list.pkl','wb')
#只有二进制可写模式,方可倒入,ab,wb效果一样的,创建一个新的,不会追加写入;文件名后缀可任意
pickle.dump(b2*2,f)
f.close()

f=open('my_list.pkl','rb')    #只能用'rb'模式来读取
b3=pickle.load(f)
print(b3)