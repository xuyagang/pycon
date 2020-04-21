import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq 

width, height  = 1366, 768

async def main():
    browser = await launch()
    # 新建页面
    page = await browser.newPage()
    # 设置页面大小
    await page.setViewport({'width':width, 'height':height})
    # 访问网页
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(3)
    await page.screenshot({'path':'./exercise/pyppeteer/example.jpg'})
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio
        }
    }''')
    print(dimensions)
    await browser.close()

asyncio.run(main())