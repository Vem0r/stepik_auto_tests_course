from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    lable1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_tag_name("button")
    button.click()
    x1 = browser.find_element_by_id('input_value').text
    y = calc(x1)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    time.sleep(5)
finally:
    time.sleep(10)
    browser.quit()