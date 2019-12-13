import requests
from requests.packages import urllib3

urllib3.disable_warnings()
resp = requests.get('https://www.12306.cn',verify=False)
print(resp.status_code)



import logging

logging.captureWarnings(True)
resp = resp = requests.get('https://www.12306.cn',verify=False)
print(resp.status_code)