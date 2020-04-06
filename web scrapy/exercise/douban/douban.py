# 在本次练习中使用一下知识：
# 多进程
# requests
# re
# pyquery
# MongoDB
# PyMongo

# 本节目标
# 用requests获取站点每页的电影列表，顺着列表获取每个详情页
# 用pyquery和正则提取电影的名称、封面、类别、上映时间、评分、剧情等
# 将结果存储到MongDB数据库
# 使用多进程实现爬取的加速

# 工作流程
# 获取单个标签下的页面url(id)



from fake_useragent import FakeUserAgentError
from fake_useragent import UserAgent
from lxml import etree
import pymysql
import redis
import requests
# 不熟练
from pyquery import PyQuery as pq
import random
import time
import re



# 获取随机ua
ua = UserAgent()
headers = {'User-Agent': ua.chrome}

def temp_proxies():
    '''proxies from https://github.com/jhao104/proxy_pool,
       用于零时测试使用，如果批量爬取需要自建ProxyPool,
    '''
    url = 'http://118.24.52.95/get_all'
    proxies = requests.get(url).json()
    proxies = [proxy['proxy'] for proxy in proxies]
    return proxies

def getPageIDs(page=1):
    '''遍历获取所有页面的电影id'''

    # 翻页的起始数字
    num = 0
    # 每页默认20个
    while num < 20 * page:
        page_base_url = f'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={num}'
        # timeout 必须大于0
        resp = requests.get(page_base_url, headers=headers, timeout=random.randint(1,3))
        movies = resp.json()['data']
        if not movies == []:
            urls = [movie['id'] for movie in movies]
            return urls
            num += 20
            print(f'-----获取{num}条-----')
        else:
            print(f'-----获取完成-----')
            break

# 要抓取的词条
# name, year, 导演, 编剧, 主演, 类型，制作国家，语言，上映日期，片长
# 别名，评分，评价认数，星级占比，剧情，演员数，演员，cover, 短评条数，影评条数，
# 是否为TOP250， 评论(后续深化)
def parse_detail(movie_id):
    '''解析页面获取数据'''

    base_url = f'https://movie.douban.com/subject/{movie_id}/'
    resp = requests.get(
                        base_url, 
                        headers=headers,
                        timeout=3).text
    data = {}
    # html初始化
    doc = pq(resp)
    # 节点获取
    # TOP250区分，是为1，否则0
    data['TOP250'] = 1 if 'top250' in resp else 0
    # 电影名
    data['MovieName'] = doc('span[property="v:itemreviewed"]').text()
    # 海报
    data['Poster'] = doc('#mainpic > a > img').attr.src
    # 年份
    # css中，无空格并列，有空格嵌套
    data['Year'] = doc('span.year').text()[1:-1]
    # 导演
    data['Director'] = doc('a[rel="v:directedBy"]').text()
    # 编剧
    data['Scenarists'] = doc('#info > span:nth-child(3) > span.attrs a').text().split()
    # 主演
    data['Stars'] = doc('#info > span.actor > span.attrs a[rel="v:starring"]').text().split()
    # 类型,text()针对多个标签获取的对象为一个字符串
    data['Types'] = doc('span[property="v:genre"]').text().split()
    data['Country'] = re.search(r'制片国家/地区:</span>(.*?)<br/>', resp).group(1)
    # split的 / 不用转义
    data['Language'] = re.search(r'语言:</span>(.*?)<br/>', resp, re.S).group(1).split('/')
    data['ReleaseTime'] = doc('span[property="v:initialReleaseDate"]').text().split()
    data['Length'] = doc('#info > span:nth-child(22)').text()
    data['Alias'] = re.search('又名:</span>(.*?)<br/>', resp, re.S).group(1).split('/')
    data['Score'] = doc('strong[class="ll rating_num"]').text()
    data['StarWeights'] = doc('span[class="rating_per"]').text()
    data['CommentNum'] = doc('span[property="v:votes"]').text().split()
    data['Story'] = ''.join([i.strip() for i in doc('span[property="v:summary"]').text().split('\n')])
    data['ShortCommentCount'] = doc('#comments-section > div.mod-hd > h2 > span > a').text().split()[1]
    # 影评数
    data['FilmReviewCount'] = doc('#content > div.grid-16-8.clearfix > div.article > section.reviews.mod.movie-content > header > h2 > span > a').text().split()[1]
    # 调用函数获取数据
    data['Celebrities'] = get_celebrities(movie_id)
    data['Summary'] = doc('span[property="v:summary"]').text().strip()

    return data

def get_celebrities(id):
    # 获取页面的演员数据
    url = f'https://movie.douban.com/subject/{id}/celebrities'
    resp = requests.get(url, headers=headers, timeout=random.randint(1,3)).text
    html = etree.HTML(resp)
    celebrities = html.xpath('//li[@class="celebrity"]')
    celebrity = {}
    for i in celebrities:
        c_name = i.xpath('./a/@title')
        c_url = i.xpath('./a/@href')
        c_role = i.xpath('//li[@class="celebrity"]/div/span[2]/text()')
        celebrity[c_name[0]] = [None if c_url == [] else c_url[0], 
                                None if c_role == [] else c_role[0]]
    return celebrity

def save_data():
    pass

def main():
    '''实现代理和多进程加速爬取'''
    # 尝试管道的使用
    pass



if __name__ == '__main__':
    id_withTOP250 = '1292064'
    id_withoutTOP250 = '26794435'
    id_test = '25662329'

    ids = getPageIDs()
    for id in ids[3:5]:
        a = parse_detail(id_test)
        print(a)
    # get_celebrities(id_test)