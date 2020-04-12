# 对响应来说，我们可以用如下的方法分别获取响应的状态码，
# 响应头，响应体，响应体二进制内容，响应体json结果

import aiohttp
import asyncio
async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as resp:
            print('status:', resp.status)
            print('headers:', resp.headers)
            print('body:', await resp.text())
            print('bytes:', await resp.read())
            print('json:', await resp.json())
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())