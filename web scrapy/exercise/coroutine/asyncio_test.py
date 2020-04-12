import asyncio

# 定义协程
async def execute(x):
    print('Number:', x)
# 返回协程对象，不能直接运行，需要加入到事件循环
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
# 创建事件循环
loop = asyncio.get_event_loop()
# 将协程注册到事件循环，并启动事件循环
loop.run_until_complete(coroutine)
print('After calling loop')


# 创建一个task
# run_until_complete方法将协程包装成一个任务，所谓任务是Futrue类的子类
# 保存了协程运行后的状态，用于未来获取协程的结果
import asyncio
import time

# 返回一个函数，调用需加括号
now = lambda : time.time()
async def do_some_work(x):
    print('Waiting：', x)
start = now()
coroutine = do_some_work(3)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print("Time:", now() - start)
'''
<Task pending coro=<do_some_work() running at d:/project/pycon/web scrapy/exercise/coroutine/asyncio_test.py:25>>    
Waiting： 3
<Task finished coro=<do_some_work() done, defined at d:/project/pycon/web scrapy/exercise/coroutine/asyncio_test.py:2
'''
# task在加如事件循环之前是pending状态
# asyncio.ensure_future() 和 loop.create_task()都可创建task
# run_until_complete的参数是一个future,传入一个协程，内部会自动封装成task
# task是future的子类， isinstance(task, asyncio.Future) 会返回True

import time
import asyncio

# 返回一个函数
now = lambda:time.time()

async def do_some_work(x):
    print('waiting:', x)

start = now()
coroutine = do_some_work(3)
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('Cost:', now() - start)