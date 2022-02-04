from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    radiobutton1 = browser.find_element_by_id('robotsRule')
    radiobutton1.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    time.sleep(5)
finally:
    time.sleep(10)
    browser.quit()