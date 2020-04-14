# 目标
# 使用aiohttp完成全站的书籍数据爬取
# 将数据通过异步的方式保存到MongDB

# 配置:
# python >=3.6, Ajax, asyncio, aiohttp, motor, MongoDB
url = 'https://dynamic5.scrape.cuiqingcai.com'

# 异步爬虫应该能够充分利用资源进行全速爬取，其思路是维护一个动态
# 变化的爬取队列，每产生一个新的task就会将其放入队列中，有专门的
# 爬虫消费者从队列中获取task并执行，能做到在最大并发量的前提下充
# 分利用等待时间进行额外的爬取处理
# 需要设计爬取队列、回调函数、消费者等机制

# 这里我们将爬取的逻辑拆分成两部分，第一部分为爬取列表页，
# 第二部分为爬取详情页。由于异步爬虫的关键点在于并发执行，
# 所以我们可以将爬取拆分为两个阶段

# 第一阶段为所有列表页的异步爬取，我们可以将所有的列表页的
# 爬取任务集合起来，声明为 task 组成的列表，进行异步爬取
# 第二阶段则是拿到上一步列表页的所有内容并解析，拿到所有书的
# id信息，组合为所有详情页的爬取任务集合，声明为task组成的列
# 表，进行异步爬取，同时爬取的结果也以异步的方式存储到MongoDB

# 两个阶段的拆分之后需要串行执行，所以可能不能达到协程的最佳调
# 度方式和资源利用情况，但也差不了很多。但这个实现思路比较简单
# 清晰，代码实现也比较简单，能够帮我们快速了解 aiohttp 的基本使用

import aiohttp
import asyncio
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    #filename='./exercise/aiohttp_example/async_scrapy.log'
    )
INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 5

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None
async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            # 指定exc_info打印traceback
            logging.error('error occurred while scraping  %s', url, exc_info=True)

async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('Results %s', json.dumps(results, ensure_ascii=False, indent=2))
    
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    # asyncio.run(main())