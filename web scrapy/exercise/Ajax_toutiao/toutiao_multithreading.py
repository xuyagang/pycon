# 分析ajax请求来抓取网页数据，获取今日头条的街拍美图

from urllib.parse import urlencode
from fake_useragent import UserAgent
from multiprocessing.pool import Pool
import requests
import random
import time
import re


num = 0
base = 'https://www.toutiao.com/api/search/content/'
# 尝试多次加了cookies才能正确访问
# ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
ua = UserAgent().chrome

cookie1 = {'tt_webid':6800150923446240776,
        's_v_web_id':'verify_k7cm4v8m_umbRkBTt_i0bZ_4UHF_BVl3_aSskHIOQD8uF',
        'WEATHER_CITY':'%E5%8C%97%E4%BA%AC',
        'tt_webid':'6800150923446240776',
        'csrftoken':'579d52997d09f6f31f074814c3ee37d9',
        'ttcid':'9e0c3a476413489baacd6ea183d99a8f76',
        'SLARDAR_WEB_ID':'d6580966-ed41-4d12-b452-9187e039503d',
        'tt_scid':'q11gUeu.2gEedNHNripGAWH5B-vNXDKYeyb991t4z0cKaxDchsPTI9tgAjquQuNZb054',
        '__tasessionId':'ceqqr9xmo1583481001451'}
cookie = '''tt_webid=6800150923446240776; s_v_web_id=verify_k7cm4v8m_umbRkBTt_i0bZ_4UHF_BVl3_aSskHIOQD8uF; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6800150923446240776; csrftoken=579d52997d09f6f31f074814c3ee37d9; ttcid=9e0c3a476413489baacd6ea183d99a8f76; SLARDAR_WEB_ID=d6580966-ed41-4d12-b452-9187e039503d; tt_scid=S.AZu9EX8Huw-B0G1HWAFT11Z9lhPd4SOSxU9BaRSHnVcFosI4hisI7mPe3UV1k31b66'''
def get_ajax_url(url, offset, keyword='油画'):
    '''获取动态加载页面的文章链接'''
    timestamp = int(time.time()*1000)
    ref = 'https://www.toutiao.com/search/?' + urlencode({'keyword':keyword})
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': True,
        # count是20，但实际并未返回20条（当时检查首页有14条）
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': timestamp
    }
    path = '/api/search/content/?' + urlencode(params)
    headers = {
        # 下面的可不添加
        # 'authority': 'www.toutiao.com',
        # 'method': 'GET',
        # 'path': path,
        # 'scheme': 'https',
        # 'accept': 'application/json, text/javascript',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'referer': ref,
        'user-agent':ua,
        'x-requested-with': 'XMLHttpRequest',
        'cookie': cookie
    }

    resp = requests.get(url, headers=headers, params=params)
    print(resp.status_code)
    data = resp.text
    pattern = r'"article_url":"(.*?)"'
    urls = re.findall(pattern, data, re.M)
    urls = ['https://www.toutiao.com/a' + i.split('/')[-2] + '/' for i in urls]
    yield urls

def get_page(urls):
    for url in urls:
        global num
        # 重新构造headers 调用有用字段
        headers={'user-agent':ua, 'cookie':cookie}
        resp = requests.get(url, headers=headers)
        # 调试有两种网页形式，可用以下字段进行区别
        # 鼠标点击切换图片模式
        key1 = 'galleryInfo'
        # 显示全部图片模式
        key2 = 'articleInfo'
        # 如果两个都没有就是西瓜视频
        data = resp.text
        if key1 in data:
            pattern = r'\.pstatp\.com\\\\\\u002Forigin\\\\\\u002F(.*?)\\"'
            imgUrls = list(set(re.findall(pattern, data, re.M)))
            imgUrls = [i.split('u002F')[-1] if 'u002F' in i else i for i in imgUrls]
            for i in imgUrls: print(i)
            base = 'http://p1.pstatp.com/origin/'
            for url in imgUrls:
                url_temp = 'pgc-image/' + url if len(url) > 21 else url
                try:
                    img = requests.get(base + url_temp, timeout=5).content
                    with open(f'D:/temp/toutiao_hc/{url}.jpg','wb') as f:
                        f.write(img)
                except:
                    print('获取失败')
                print('写入图片成功---{}---'.format(num))
                num += 1
        elif key2 in data:
            base = 'http://p3.pstatp.com/large/pgc-image/'
            pattern = r'\\u002Flarge\\u002Fpgc-image\\u002F(.*?)\\&quot'
            imgUrls = list(set(re.findall(pattern, data, re.M)))
            print(imgUrls)
            for url in imgUrls:
                try:
                    img = requests.get(base + url, timeout=5).content
                    with open(f'D:/temp/toutiao_hc/{url}.jpg','wb') as f:
                        f.write(img)
                except:
                    print('获取失败')
                print('写入图片成功---{}---'.format(num))
                num += 1
        else:
            pass


def main(offset):
    pageUrls = get_ajax_url(base, offset, keyword='美腿')
    for pageurl in pageUrls:
        get_page(pageurl)
        time.sleep(random.uniform(1,3))


if __name__ == '__main__':
    pool = Pool()
    groups = (i*20 for i in range(100))
    pool.map(main, groups)
    pool.close()
    pool.join()


