import requests
headers={
    'Cookie': '浏览器登录获取的cookie',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
r = requests.get('https://github.com',headers=headers)
print(r.text)


# 另外一种cookie的应用方式
headers = {'User-Agent': 'ua'}
cookies = '复制的cookie'
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get(url, cookie=jar, headers=headers)