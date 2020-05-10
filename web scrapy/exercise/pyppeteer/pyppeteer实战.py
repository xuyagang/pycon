# https://github.com/Python3WebSpider/ScrapeDynamic2/blob/master/spider2.py

import os 
import json
from os import path 
RESULTS_DIR = 'results'
path.exists(RESULTS_DIR) or os.makedirs(RESULTS_DIR)


import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False
from pyppeteer import launch



# 初始化pyppeteer的步骤
browser, tab = None, None
async def init():
    global browser, tab
    # 创建浏览器要用异步等待
    browser = await launch(
        headless=HEADLESS,
        args=['--disable-infobars',
        f'--window-size={WINDOW_WIDTH}, {WINDOW_HEIGHT}'])
    # 打开新窗口
    tab = await browser.newPage()
    # 设置窗口
    await tab.setViewport({'width': WINDOW_WIDTH, 
                           'height': WINDOW_HEIGHT})

# 定义通用爬取方法
from pyppeteer.errors import TimeoutError
async def scrape_page(url, seletor):
    # logging 自带的字符格式化方法
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(seletor, options={
            # visible, hidden, timeout(milliseconds)
            'timeout': TIMEOUT * 1000
        })
    except TimeoutError:
        logging.info('error occurred while scraping %s', 
        url, exc_info=True)

# 爬取列表页的方法
async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    # querySelectorAllEval 方法，它接收两个参数，
    # 第一个参数是 selector，代表要选择的节点对应的 CSS 选择器；
    # 第二个参数是 pageFunction，代表的是要执行的JavaScript方法
    await scrape_page(url, '.item .name')

async def parse_index():
    # 提取出每部电影的详情页 URL
    return await tab.querySelectorAllEval('.name', 
    # 类似py的map,map() 方法返回一个新数组，
    # 数组中的元素为原始数组元素调用函数处理后的值
    'nodes => nodes.map(node => node.href)')

async def scrape_detail(url):
    # 等待每个网页的目标元素在标签页加载完成
    await scrape_page(url, 'h2')

# 接下来获取详情页
async def parse_detail():
    # URL、名称、类别、封面、分数、简介
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.innerText')
    categories = await tab.querySelectorAllEval(
        '.categories button span', 'nodes => nodes.map(node => node.inderText)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.innerText')
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


# 我们使用的是 Pyppeteer，是异步调用，所以 save_data 方法前面需要加 async
async def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}\{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), 
              ensure_ascii=False, indent=2)

import asyncio
async def main():
    await init()
    try: 
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('data %s', detail_data)
                await save_data(detail_data)
    finally:
        await browser.close()
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
