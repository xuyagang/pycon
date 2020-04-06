from selenium import webdriver
from selenium.webdriver.common.by import By

# 生成浏览器对象
browser = webdriver.Chrome()
# 发起请求
browser.get('https://www.taobao.com/')
# 获取对象
# lis = browser.find_elements(By.XPATH, '//ul[@class="service-bd"]//a')
lis = browser.find_elements(By.CSS_SELECTOR, 'ul.service-bd li a')
print(lis)
browser.close()