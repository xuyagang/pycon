# 对于post表单提交，其对应的请求头的 Content-type 为 
# application/x-www-form-urlencoded，我们可以用如下方式来实现

import aiohttp
import asyncio

async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print(await response.text())

# 对于post json数据提交，其对应的请求头的content-type：application/json
# 只需要将post方法对应的data参数改外json即可
async def main1():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', json=data) as resp:
            print(await resp.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main1())
    