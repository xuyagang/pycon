import requests

# 如果代理需要认证，同样在代理的前面加上用户名密码即可
# proxy = 'username:password@127.0.0.1:7890'
proxy = '27.43.186.155:9999'
proxies = {
    'https': 'https://' + proxy,
    'http': 'http://' + proxy,
}
url = 'https://httpbin.org/get'
try:
    resp = requests.get(url, proxies=proxies)
    print(resp.text)
except requests.ConnectionError as e:
    print(str(e))
    print("Error", e.args)


# SOCKS 代理
import requests
proxy = '27.43.186.155:9999'
proxies = {
    'https': 'socks5://' + proxy,
    'http': 'sock5://' + proxy,
}
url = 'https://httpbin.org/get'
try:
    resp = requests.get(url, proxies=proxies)
    print(resp.text)
except requests.ConnectionError as e:
    print(str(e))
    print("Error", e.args)


# 使用socks模块
import requests
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7891)
socket.socket = socks.socksocket
try:
    resp = requests.get(url)
    print(resp.text)
except requests.ConnectionError as e:
    print(e.args)
    