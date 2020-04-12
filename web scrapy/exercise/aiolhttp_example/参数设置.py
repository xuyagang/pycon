import asyncio
import aiohttp

async def main():
    # params = {'names': 'Germey', 'age': 25}
    # 同键不同值的并联字典
    # 使用带有两个tuples(元组，python中的数据类型)的list(列表，
    # python中的数据类型)来构建
    params = [('key', 'value1'), ('key', 'value2')]
    async with aiohttp.ClientSession() as sesssion:
        async with sesssion.get(
            'https://httpbin.org/get',
            params=params) as response:
            print(await response.text())
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

