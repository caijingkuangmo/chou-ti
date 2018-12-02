from django.test import TestCase

# Create your tests here.
import redis

#连接池一般采用单例模式，可以和django admin里的site对象，通过导入实现单例
redis_pool = redis.ConnectionPool(host="localhost", port="6379")

conn = redis.Redis(connection_pool=redis_pool)
# conn = redis.Redis(host="localhost", port=6379)

#单次操作
conn.set('email', '123')
print(conn.get('email'))


#事务操作
pipe = conn.pipeline(transaction=True)
pipe.multi()

pipe.set('k2', 123)
pipe.hset('k3', 'n1', 456)
pipe.lpush('k4', 789)
pipe.execute()

print(conn.get('k2'))
print(conn.hget('k3', 'n1'))
print(conn.lpop('k4'))


