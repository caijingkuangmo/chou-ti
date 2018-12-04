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
import redis
redis_pool = redis.ConnectionPool(host="localhost", port=6379)
conn = redis.Redis(connection_pool=redis_pool)
# conn.mset({'k100':'v100', 'k200':'v200'})
# print(conn.mget('k100', 'k200'))
# print(conn.mget(['k100','k200']))

# conn.append('k100', '00000000000000')


# conn.set('number', 0)
# conn.incr('number')
# conn.incr('number')
# conn.incr('number') #3

# conn.hmset('xx', {'k1':'k1', 'k2':'k2'})
print(conn.hmget('xx', ['k1', 'k2']))
print(conn.hmget('xx', 'k1', 'k2'))