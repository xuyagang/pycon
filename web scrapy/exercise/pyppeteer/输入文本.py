import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq 

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    # 输入文本
    await page.type('#q', 'iPad')
    # 关闭
    await asyncio.sleep(5)
    await browser.close()

asyncio.run(main())