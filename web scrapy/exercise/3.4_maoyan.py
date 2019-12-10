# 目标：获取TOP100的电电影名称、时间、评分、图片等信息

# 站点分析
# https://maoyan.com/board/4?offset=0
# https://maoyan.com/board/4?offset=10
# https://maoyan.com/board/4?offset=20


# 抓取首页
import requests
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





def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()