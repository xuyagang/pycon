import asyncio
import aiohttp
import time

def reqTest(reqNum):
    start = time.time()

    async def get(url):
        # 请求方法
        session = aiohttp.ClientSession()
        resp = await session.get(url)
        await resp.text()
        await session.close()
        return resp
    
    async def request():
        # 将请求封装成协程
        url = 'https://www.baidu.com'
        await get(url)
    
    tasks = [asyncio.ensure_future(request()) for _ in range(reqNum)]
    loop = asyncio.get_event_loop()
    # task的列表可以通过asyncio.wait()包装成Future事件对象
    loop.run_until_complete(asyncio.wait(tasks))
    
    end = time.time()
    print("Number:", reqNum, 'Cost time:', end - start)

for num in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    reqTest(num)