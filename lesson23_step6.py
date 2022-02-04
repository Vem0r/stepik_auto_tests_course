from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x1 = browser.find_element_by_id('input_value').text
    y = calc(x1)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(5)
finally:
    time.sleep(10)
    browser.quit()