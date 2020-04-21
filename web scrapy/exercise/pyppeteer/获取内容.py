import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq 

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    # 进入网页
    await page.goto('https://www.taobao.com')
    # 获取内容
    print('HTML:', await page.content())
    print('Cookies:', await page.cookies())
    await browser.close()

asyncio.run(main())