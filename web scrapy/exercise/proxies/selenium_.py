from selenium import webdriver
url = 'https://httpbin.org/get'


# 常规设置
proxy = '183.166.110.9:9999'
# 浏览器选项对象
options = webdriver.ChromeOptions()
# 添加代理参数
options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(options=options)
browser.get(url)
print(browser.page_source)
browser.close()


# 认证代理
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import zipfile
#  
# ip = '127.0.0.1'
# port = 7890
# username = 'foo'
# password = 'bar'
#  
# plugin_file = 'proxy_auth_plugin.zip'
# with zipfile.ZipFile(plugin_file, 'w') as zp:
#    zp.writestr("manifest.json", manifest_json)
#    zp.writestr("background.js", background_js)
# options = Options()
# options.add_argument("--start-maximized")
# options.add_extension(plugin_file)
# browser = webdriver.Chrome(options=options)
# browser.get('https://httpbin.org/get')
# print(browser.page_source)
# browser.close()

# SOCKS 代理
from selenium import webdriver
proxy = '127.0.0.1:7891'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://'+proxy)
browser = webdriver.Chrome(options=options)
browser.get(url)
print(browser.page_source)
browser.close()