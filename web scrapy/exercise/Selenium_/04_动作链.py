from selenium import webdriver
from selenium.webdriver import ActionChains
import time




url = 'https://www.geetest.com/show'
browser = webdriver.Chrome()
browser.get(url)
# 找到元素
button = browser.find_element_by_css_selector('div.tab-item.tab-item-1')
# button = browser.find_element_by_xpath('//div[@class="tab-item tab-item-1"]')
button.click()
browser.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')
time.sleep(3)
browser.close()
