
list1=[11,4,-9,27,89,3,-37]
'''
#写法一:compare函数在函数内部定义

def sort(lst,asc=False):
	def compare(a,b):
		return a<b if asc else a>b

	newlist=[]
	for x in lst:
		for i,y in enumerate(newlist):
			if compare(x,y):    #x,y为调用的实参
				newlist.insert(i,x) #旧列表元素与新列表元一个个拿出比较,符合条件占用新列表原位置
				break
		else:
			newlist.append(x)
	return newlist

print(sort(list1,True))



#写法2:compare函数与此业务不相关定义在外面
def compare(a,b):
	return a<b

def sort(lst,fn):
	newlist=[]
	for x in lst:
		for i,y in enumerate(newlist):
			if fn(x,y):    #x,y为调用的实参
				newlist.insert(i,x) 
				break
		else:
			newlist.append(x)
	return newlist

print(sort(list1,compare))   #将compare函数传进去

'''


#写法3:将匿名函数作为参数传入



def sort(lst,fn=lambda a,b:a<b):
	newlist=[]
	for x in lst:
		for i,y in enumerate(newlist):
			if fn(x,y):    #x,y为调用的实参
				newlist.insert(i,x) 
				break
		else:
			newlist.append(x)
	return newlist

print(sort(list1,lambda x,y:x<y))
print(sort(list1,lambda x,y:x>y))







