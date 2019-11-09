# coding:utf-8

from redis import StrictRedis
#连接Redis
rs = StrictRedis(host='localhost',port=6379,db= 0,password=None)
#创建键值对
rs.set('name','test')
#打印name键的值
print(rs.get('name'))

