import requests
# 请求并设置cookies为123456
requests.get('http://httpbin.org/cookies/set/number/123456')
# 随后又请求一次,可以获取当前cookies
r = requests.get('http://httpbin.org/cookies')
print(r.text)
'''
{
  "cookies": {}
}
'''


# 我们用session试试
s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456')
r = s.get('http://httpbin.org/cookies')
print(r.text)