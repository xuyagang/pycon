import requests
data = {
    'name': 'adam',
    'age':18
}

r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
st = r.json()
print(type(st))

'''
{
  "args": {
    "age": "18",
    "name": "adam"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-5e762fea-6e9656e6398aab9ae01264b2"
  },
  "origin": "118.112.58.226",
  "url": "http://httpbin.org/get?name=adam&age=18"
}
'''