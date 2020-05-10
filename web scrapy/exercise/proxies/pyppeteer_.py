import asyncio
from pyppeteer import launch

proxy = '127.0.0.1:7891'
async def main():
    browser = await launch({
        'args':['--proxy-sever=http://' + proxy],
        'headless': False
    })
    page = await browser.newPage()
    await page.goto(url)
    print(await page.content())
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


# 对于 SOCKS 代理，也是一样的，只需要将协议修改为 socks5 即可