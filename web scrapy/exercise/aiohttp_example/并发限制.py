# 借助asyncio的Semaphore
import aiohttp
import asyncio

# 最大并发量
CONCURRENCY = 5
URL = 'https://www.baidu.com'
# 创建信号量对象，控制最大并发量
# 放置于对应的爬取方法里面，使用async with 语句将semaphore作为上下文对象即可
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None
async def scrape_api():
    async with semaphore:
        print('scraping', URL)
        async with session.get(URL) as resp:
            await asyncio.sleep(1)
            return await resp.text()
async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrape_index_tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())