# from redis import StrictRedis
# redis = StrictRedis(host='localhost', port=6379, db=0, password='devil')
# redis.set('name','Bob')
# print(redis.get('name'))



# from redis import StrictRedis, ConnectionPool
# pool = ConnectionPool(host='localhost', port=6379, db=0, password='devil')
# redis = StrictRedis(connection_pool=pool)
'''
这样的连接效果是一样的，观察源码可发现，StrictRedis内其实就是用host和port等参数
又构造了一个ConnectionPool,所以直接将ConnectionPool当作参数传给StrictRedis也
一样，另外也通过url来构造，url的格式支持如下三种：
redis://[:password]@host:port/db
rediss://[:password]@host:port/db
unix://[:password]@/path/to/socket.sock?db=db
'''


from redis import StrictRedis, ConnectionPool
url = 'redis://:devil@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('hello', 'world')
value = redis.get('hello')
print(value)
redis.setnx()