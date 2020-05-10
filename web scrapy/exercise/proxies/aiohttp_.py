# 常规设置
import aiohttp
import asyncio

proxy = 'http://127.0.0.1:7891'
url = ''
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', proxy=proxy) as resp:
            print(await resp.text())

# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())

# 认证代理
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            proxy = 'http://127.0.0.1:7891',
            proxy_auth = 'proxy_auth') as resp:
            print(resp.status)

# url方式
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            proxy='http://user:passwd@127.0.0.1:7891') as resp:
            print(resp.text())

# socks
import aiohttp
import asyncio
from aiohttp_socks import PorxyConnector

connector = PorxyConnector.from_url('socks5://127.0.0.1:7891')
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())