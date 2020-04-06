MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'


import redis
from random import choice

class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, passwd=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, passward=passwd, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        '''
        添加代理，设置分数为最高
        '''
        # 获取有序集合中成员的分数值
        if not self.db.zscore(REDIS_KEY, proxy):
            # 添加，存在则更新
            return self.db.zadd(REDIS_KEY, score, proxy)
    
    def random(self):
        '''
        随机获取有效代理，首先尝试获取最高分数代理，如果不存在则按照排名获取，否则异常
        '''
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
                else:
                    raise PoolEmptyError
    
    def decrease(self, proxy):
        '''代理值减一分，小于最小值则删除'''
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        '''判断是否存在'''
        return not self.db.zscore(REDIS_KEY, proxy) == None
    
    def max(self, proxy):
        '''将代理设置为max_score'''
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        '''获取数量'''
        return self.db.zcard(REDIS_KEY)
    
    def all(self):
        '''获取全部代理'''
        self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
    

    
    
        
