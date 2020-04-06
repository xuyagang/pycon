from selenium import webdriver
from selenium.webdriver import ActionChains



browser = webdriver.Chrome()
# browser.maximize_window()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_css_selector('a[aria-label="知乎"] > svg')
print(logo.get_attribute('width'))

button = browser.find_element_by_css_selector('a.ExploreSpecialCard-title')
print(button.text)
# button.click()
print(button.id)
print(button.location)
print(button.size)
print(button.tag_name)