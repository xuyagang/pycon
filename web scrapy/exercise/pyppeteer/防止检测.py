import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://antispider1.scrape.cuiqingcai.com/')
    await asyncio.sleep(20)
asyncio.run(main())