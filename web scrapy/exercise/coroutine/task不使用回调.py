# 不使用回调方法,直接在task运行完成后直接调用result方法获取结果
import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

coroutine = request()
task = asyncio.ensure_future(coroutine)
print('Task:', task)

loop = asyncio.get_event_loop()
# 次方法不用赋值
loop.run_until_complete(task)
print('Task:', task)
print('Task Result:', task.result())