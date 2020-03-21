from multiprocessing import Pool
import requests

def scraped(url):
    try:
        resp = requests.get(url)
        print(f'URL {url} scraped')
    except:
        print(f'URL {url} not Scraped')

if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com',
        'http://blog.csdn.net/',
        'http://xxxyyyzz.net'
    ]
    pool.map(scraped, urls)
    pool.close()