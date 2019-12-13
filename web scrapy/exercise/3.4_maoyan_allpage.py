# 目标：获取TOP100的电电影名称、时间、评分、图片等信息

# 站点分析
# https://maoyan.com/board/4?offset=0
# https://maoyan.com/board/4?offset=10
# https://maoyan.com/board/4?offset=20


# 抓取首页
import requests
import re
import json
import time
import random


def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        # 'Accept-Language':'zh-CN'
    }
    response = requests.get(url, headers=headers)
    # response.encoding='utf-8'
    if response.status_code == 200:
        return response.text
    return None

# 在开发者模式下的Network监听组件中查看源代码，查看原始请求的代码
# 与Elements选项卡中的源代码不同，那里的源代码可能经过JavaScript操作而与原始的请求不同
# 在network处搜索关键字即可定位

# 使用正则表达式定位
def parse_one_page(html):
    # board_index,href,title,star,releasetime,score
    # 括号（（）），方括号（[]）,大括号({})==可以让一个语句的范围横跨多行
     pattern = re.compile('<dd>.*?board-index.*?(\d+)</i>.*?href="(.*?)" title="(.*?)".*?<img data-src="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">.*?(.*?)</p>.*?class="score"><i class="integer">(.*?)</i>.*?</dd>',
     flags=re.S)
    # findall和split获取结果是list
     items= re.findall(pattern, html)
     for item in items:
         yield {
             'index': item[0],
             'film_href': item[1],
             'title': item[2],
             'image': item[3],
             'star': item[4].strip()[3:],
             'releasetime': item[5][5:].strip(),
             'score': item[6],
         }
    #  print(items)

# 写入文件
# 对于字典类型数据，通过json的dumps方法将数据写入文本
def write_to_file(content):
    with open('./maoyan/maoyan_all_page_data.txt', 'a', encoding='utf-8') as f:
        # 将字典转为字符串
        content = json.dumps(content, ensure_ascii=False)
        f.write(content+'\n')



def main():
    base_url = 'https://maoyan.com/board/4'
    for i in range(0,100,10):
        url = base_url + '?offset='+str(i)
        html = get_one_page(url)
        for item in parse_one_page(html):
            write_to_file(item)
    
    time.sleep(random.randint(0,3))

    # print(html)
    # print(list(parse_one_page(html)))

main()