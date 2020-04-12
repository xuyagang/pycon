# 协程在解决IO密集任务上的优势

# 耗时等待的操作一般都是 IO 操作，比如文件读取、网络请求等等。
# 协程对于处理这种操作是有很大优势的，当遇到需要等待的情况的时候，
# 程序可以暂时挂起，转而去执行其他的操作，从而避免一直等待一个
# 程序而耗费过多的时间，充分利用资源

import asyncio
import requests
import time
import aiohttp


start = time.time()
async def get(url):
    requests.get(url)
async def request():
    url = 'https://static4.scrape.cuiqingcai.com/'
    print('Waiting for:', url)
    # await 可以将耗时等待的操作挂起，让出控制权
    # 当协程执行遇到await，时间循环会将本协程挂起，转而执行别的协程，
    # 直到其他协程挂起或执行完毕
    resp = await get(url)
    print("Get response from", url, 'Response', resp)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
# wait 用于处理多任务
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("cost time:", end-start)