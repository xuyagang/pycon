import aiohttp
import asyncio
import time

start = time.time()
url = 'https://static4.scrape.cuiqingcai.com/'

async def get(url):
    # 创建会话
    session = aiohttp.ClientSession()
    # 遇到阻塞的时候，await让出控制权，以便loop调用其他协程
    resp = await session.get(url)
    print('获取页面内容')
    # 异步请求的响应获取前要加await,不然得到一个对象
    # <coroutine object ClientResponse.text at 0x000002BDE13C56C8>
    print('直接获取内容:', await resp.text())
    return resp

async def request():
    resp = await get(url)
    print('异步获取')
    print("Get response from:", url, 'Response:', resp)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
# asyncio.wait()给出完成和挂起的任务，需传入a list of futures, not coroutine
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("Cost time:", end - start)