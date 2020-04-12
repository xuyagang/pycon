import asyncio
import requests

# 定义协程
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

def callback(task):
    # 接受task对象，打印task的结果
    print('Status:', task.result())

# 返回协程对象
coroutine = request()
# 创建任务
task = asyncio.ensure_future(coroutine)
# 任务创建后,调用callback方法,只需要调用 add_done_callbakc方法即可
# task对象会作为参数传递给callback,最后调用task对象的result方法获取结果
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)



