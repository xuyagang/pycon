import requests

files = {'file': open('./exercise/requests/001.png', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)