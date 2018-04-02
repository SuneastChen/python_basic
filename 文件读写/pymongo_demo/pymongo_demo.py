# _*_ coding:utf-8 _*_
# !/usr/bin/python

from pymongo import MongoClient

mc = MongoClient('localhost', 27017)  # 连接数据库
db = mc.mydb  # use mydb数据库
db.user.save({'name': '张三', 'age': 90})  # 将记录写入表
# 查询记录
print([d for d in db.user.find({'name': 'chengxudong'})])
data_obj = db.user.find()
for o in data_obj:
    print(o)
print([d for d in data_obj])
mc.close()  # 关闭与数据库连接
