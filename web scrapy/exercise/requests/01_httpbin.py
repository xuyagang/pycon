import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

'''
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-5e762eef-4e8f964cadba61789d7a899a"
  },
  "origin": "118.112.58.226",
  "url": "http://httpbin.org/get"
}
'''
# 我们发起了请求，网站返回了请求所携带的信息