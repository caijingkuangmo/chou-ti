from __future__ import division
from django.test import TestCase

# Create your tests here.

'''
redis 管道
'''
# import redis
#
# #连接池一般采用单例模式，可以和django admin里的site对象，通过导入实现单例
# redis_pool = redis.ConnectionPool(host="localhost", port="6379")
#
# conn = redis.Redis(connection_pool=redis_pool)
# # conn = redis.Redis(host="localhost", port=6379)
#
# #单次操作
# conn.set('email', '123')
# print(conn.get('email'))
#
#
# #事务操作
# pipe = conn.pipeline(transaction=True)
# pipe.multi()
#
# pipe.set('k2', 123)
# pipe.hset('k3', 'n1', 456)
# pipe.lpush('k4', 789)
# pipe.execute()
#
# print(conn.get('k2'))
# print(conn.hget('k3', 'n1'))
# print(conn.lpop('k4'))


'''
__getattr__
__setattr__
'''
# class Foo:
#
#     def __getattr__(self, item):
#         print(item)
#
#     def __setattr__(self, key, value):
#         print(key, value)
#
# obj = Foo()
# obj.xx = 123
# obj.xx


'''
redis 操作
'''
# import redis
# redis_pool = redis.ConnectionPool(host="localhost", port=6379)
# conn = redis.Redis(connection_pool=redis_pool)
# conn.mset({'k100':'v100', 'k200':'v200'})
# print(conn.mget('k100', 'k200'))
# print(conn.mget(['k100','k200']))

# conn.append('k100', '00000000000000')


# conn.set('number', 0)
# conn.incr('number')
# conn.incr('number')
# conn.incr('number') #3

# conn.hmset('xx', {'k1':'k1', 'k2':'k2'})
# print(conn.hmget('xx', ['k1', 'k2']))
# print(conn.hmget('xx', 'k1', 'k2'))

# conn.lpush('xx', 11, 22, 33)
# conn.lpushx('oo', 11)
# conn.lpushx('xx', 11)

# conn.linsert('xx', 'BEFORE', '33', '8888')
#
# conn.lre
#
# def list_iter(name):
#     list_count = conn.llen(name)
#     for index in range(list_count):
#         yield conn.lindex(name, index)
#
# for item in list_iter('xx'):
#     print(item)

#排序
# p = [{'name':'Jon','age':32},{'name':'Alan','age':50},{'name':'Jon','age':23}]
# print(sorted(p, key=lambda item: (item['name'], item['age'])))
#
# p.sort(key=lambda x: x['age'], reverse=True)
# print(p)

#计数
# from collections import defaultdict
# data = ['a','2',2,3,4,'2','b','a','b',3,4,'a']
# count_frq = defaultdict(int)
# for item in data:
#     count_frq[item] += 1
# print(count_frq)

# from collections import Counter
# data = ['a','2',2,3,4,'2','b','a','b',3,4,'a']
# print(Counter(data))
# print(Counter(data).most_common(3))  #获取出现频率最高的三个


# 追踪错误信息
# import traceback
# gList = ['a','b','c','d','e','f','g']
# def f():
#     gList[5]
#     return g()
# def g():
#     return h()
# def h():
#     del gList[2]
#     return i()
# def i():
#     gList.append('i')
#     print(gList[7])
# if __name__ == '__main__':
#     try:
#         f()
#     except IndexError as ex:
#         print("Sorry,Exception occured,you accessed an element out of range")
#         print(ex)
#         traceback.print_exc()


import logging

# create logger
logger = logging.getLogger('DEBUG-LOG')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler("log/access.log")
fh.setLevel(logging.WARNING)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')