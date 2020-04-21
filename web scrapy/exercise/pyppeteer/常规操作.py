import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://dynamic1.scrape.cuiqingcai.com/')
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    # 后退
    await page.goBack()
    # 前进
    await page.goForward()
    # 刷新
    await page.reload()
    # 保存pdf
    await page.pdf({'path':'test.pdf'})
    # 截图
    await page.screenshot({'path':'screenshotTest.jpg'})
    # 设置页面 HTML
    await page.setContent('<h2>Hello World</h2>')
    # 设置User-Agent
    await page.setUserAgent('python')
    # 设置Headers
    await page.setExtraHTTPHeaders(headers={})
    # 关闭
    await page.close()
    await browser.close()
asyncio.run(main())