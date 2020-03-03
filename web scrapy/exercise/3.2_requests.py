import requests

r = requests.get('https://baidu.com')
print(type(r))
# <class 'requests.models.Response'>
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>


r = requests.get('http://httpbin.org/get')
r.encoding= 'utf-8'
print(r.text)