import asyncio
from pyppeteer import launch 
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    await page.click('.item .name', options={
        'button': 'right',
        'clickCount': 1,
        'delay': 3000         # 毫秒
    })
    await browser.close()

asyncio.run(main())