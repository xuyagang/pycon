import asyncio
import time

now = lambda:time.time()
async def do_some_work(x):
    print(f'waiting{x} s')
    return f'Done after {x} s'

start = now()

coroutine = do_some_work(3)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("Task result:{}".format(task.result()))
print('Time:{}'.format(now()-start))