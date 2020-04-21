import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # 定义异步浏览器
    browser = await launch()
    # 创建页面
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    # 等待加载
    await page.waitForSelector('.item .name')
    j_result1 = await page.J('.item .name')
    j_result2 = await page.querySelector('.item .name')
    jj_result1 = await page.JJ('.item .name')
    jj_result2 = await page.querySelectorAll('.item .name')
    print('J Result1: ', j_result1)
    print('J Result2: ', j_result2)
    print('JJ Result1: ', j_result1)
    print('JJ Result2: ', j_result2)

    await browser.close()
asyncio.run(main())