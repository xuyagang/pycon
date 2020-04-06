import redis

db = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='devil',
    db=0,
    decode_responses=False)
db.set('foo', 'bar')

# 
pool = redis.ConnectionPool(
    host='127.0.0.1', 
    port=6379, 
    db=0,
    password='devil'
)
conn = redis.Redis(connection_pool=pool)
conn.set('hello','world')