import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # launch 方法会新建一个 Browser 对象，其执行后最终会得到一个 Browser 对象，
    # 然后赋值给 browser。这一步就相当于启动了浏览器
    browser = await launch()
    # browser 调用 newPage  方法相当于浏览器中新建了一个选项卡，同时新建了一个 Page 对象，
    # 这时候新启动了一个选项卡，但是还未访问任何页面，浏览器依然是空白
    page = await browser.newPage()
    # 调用了 goto 方法就相当于在浏览器中输入了这个 URL，
    # 浏览器跳转到了对应的页面进行加载
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    # Page对象调用waitForSelector方法，传入选择器，那么页面就会等待选择器所对应的节点信息
    # 加载出来，如果加载出来了，立即返回，否则会持续等待直到超时。
    # 此时如果顺利的话，页面会成功加载
    await page.waitForSelector('.item .name')
    # 页面加载完成之后再调用 content 方法，可以获得当前浏览器页面的源代码
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
# 免去了一些烦琐的步骤，同样达到了 Selenium 的效果，还实现了异步抓取