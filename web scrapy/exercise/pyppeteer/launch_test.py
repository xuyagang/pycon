import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(20)

asyncio.run(main())