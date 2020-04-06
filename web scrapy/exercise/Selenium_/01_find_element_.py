from selenium import webdriver

# 浏览器对象
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.safari()

# 发起请求
browser.get('https://www.taobao.com')
# 查找元素
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third, sep='\n')
browser.close()