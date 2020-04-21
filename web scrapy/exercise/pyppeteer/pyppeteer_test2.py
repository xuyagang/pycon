import asyncio
from pyppeteer import launch
width, height = 1366, 768

async def main():
    # 浏览器和窗口需要异步创建
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(3)
    # screenshot方法可传入图片路径，保存格式type,清晰度quality,
    # 是否全屏fullpage,裁切clip等各个参数实现截图
    await page.screenshot(path='./exercise/pyppeteer/example.png')
    # deviceScaleFactor:像素大小比率
    dimensions = await page.evaluate(
        '''() => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio
            }
        }
        ''')
    print(dimensions)
    await browser.close()
asyncio.run(main())