from selenium import webdriver


browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
print(browser.current_window_handle)
button = browser.find_element_by_css_selector('a.ExploreSpecialCard-title')
button.click()
print(browser.current_window_handle)
