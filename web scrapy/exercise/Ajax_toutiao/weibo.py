# 用程序模拟ajax请求，爬取前n页微博头条

import time
import requests
# 将字典数据编码为url
from urllib.parse import urlencode
from lxml import etree
# https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=1760&page=3&lefnav=0&cursor=&__rnd=1583075905362
from pymongo import MongoClient






baseUrl = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?'
now = int(time.time()*1000)
page_nums = [i for i in range(1,11)]
headers = {
    'Host': 'weibo.com',
    'Referer': 'https://weibo.com/?topnav=1&mod=logo',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def getPage(page_num):
    parameters = {
        'ajwvr':6,
        'category':1760,
        # 用于控制页面
        'page':page_num,
        'lefnav':0,
        'cursor':'',
        '__rnd': now
    }
    url = baseUrl + urlencode(parameters)
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            print('获取成功')
            return resp.json()
            # print(resp.json())
    except requests.ConnectionError as e:
        print('Error:', e.args)

def parse_page(data):
    # 获取微博id, 正文, 赞数, 评论数, 转发
    if data:
        html = etree.HTML(data.get('data'))
        items = html.xpath('//div[@class="UG_list_b"]')
        for item in items:
            weibo = {}
            # 标题
            weibo['titles'] = item.xpath('./div/h3/a/text()')[0]
            # 链接
            weibo['hrefs'] = item.xpath('./div/h3/a/@href')[0]
            # 博主
            weibo['authors'] = item.xpath('./div/div/a[2]//text()')[0]
            # 转发
            weibo['forwards'] = item.xpath('./div/div/span[6]/em[2]/text()')[0]
            # 评论
            weibo['comments'] = item.xpath('./div/div/span[4]/em[2]/text()')[0]
            # 点赞
            weibo['likes'] = item.xpath('./div/div/span[2]/em[2]/text()')[0]
            yield weibo
            # print(weibo)

# 写入数据库
client = MongoClient(host='localhost', port=27017)
# client = MontoClient('mongodb://localhost:27017/')
db = client['weibo']
collection = db['remen']
def save_to_mongo(data):
    if collection.insert(data):
        print('saved to mongo')


if __name__ == '__main__':
    for i in range(10):
        data = getPage(i)
        # parse_page(data)
        save_to_mongo(parse_page(data))