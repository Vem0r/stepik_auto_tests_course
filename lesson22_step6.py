from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x1 = browser.find_element_by_tag_name('wtf').text
    y = calc(x1)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton1 = browser.find_element_by_id('robotsRule')
    radiobutton1.click()
    button.click()
    time.sleep(5)
finally:
    time.sleep(10)
    browser.quit()
