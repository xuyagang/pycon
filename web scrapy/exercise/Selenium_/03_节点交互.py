# 打开网站，find_element获取输入框，
# send_keys输入文字，find_elements获取搜索结果，click完成搜索

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
input = brower.find_element(By.ID, 'q')
input.send_keys('灯具')
time.sleep(2)
input.clear()
input.send_keys('iPad')
button = brower.find_element(By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')
button.click()