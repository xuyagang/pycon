# 对于超时设置，我们可以借助ClientTimeout对象, 
# 比如这里我要设置1秒的超时
import aiohttp
import asyncio

async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://httpbin.org/get') as resp:
            print('Status:', resp.status)
            
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())