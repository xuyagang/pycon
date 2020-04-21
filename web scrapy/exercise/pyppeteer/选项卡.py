import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.bing.com')
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    pages = await browser.pages()
    print('Pages:', pages)
    page1 = pages[1]
    await page1.bringToFront()
    await asyncio.sleep(20)
    
asyncio.run(main())