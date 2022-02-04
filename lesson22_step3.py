from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element_by_id('num1')
    int_x = int(x.text)
    y = browser.find_element_by_id('num2')
    int_y = int(y.text)
    sum2 = str(int_x + int_y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum2)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    time.sleep(5)
finally:
    time.sleep(10)
    browser.quit()
