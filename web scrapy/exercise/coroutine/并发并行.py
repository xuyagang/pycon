# 使用async定义协程对象，await可以针对耗时操作进行挂起，
# 类似生成器里的yield,函数让出控制权
# 协程遇到await,事件循环将会挂起该协程，执行别的协程，直到其他协程也挂起或执行完
# 再执行下一个协程

# 耗时操作一般是IO操作，类如网路请求，文件读取
# 我们用asyncio.sleep来模拟IO操作，实现异步
import asyncio
import time

now = lambda: time.time()

async def do_some_work(x):
    print("waiting:", x)
    # 遇到阻塞函数的时候，await让出控制权，以便loop调用其他协程
    await asyncio.sleep(x)
    return f"Done after {x} s"
start = now()

coroutine = do_some_work(3)
coroutine1 = do_some_work(5)
coroutine2 = do_some_work(7)

tasks = [
    asyncio.ensure_future(coroutine),
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
# 对于多个任务组合的，需要遍历获取任务的结果
for task in tasks:
    print('Result:', task.result())
print("Time:", now()-start)