import asyncio
import aiohttp
async def fetch(session, url):
    # 利用session和url 构造发起请求获取数据的方法
    async with session.get(url) as resp:
        return await resp.text(), resp.status
async def main():
    # 构造session，利用请求方法发起请求
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html:{html[:100]}...')
        print(f'status: {status}')
        
        
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     # 需传入一个Feture对象，可使用 asyncio.wait( a list of futures, not coroutine)
#     # 生成，也可直接传入一个coroutine,会被包装成一个task
#     loop.run_until_complete(main())
    
# py3.7 + 版本中，主程序的运行代码等价于
if __name__ == '__main__':
    # Run a coroutine
    asyncio.run(main())