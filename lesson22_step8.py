from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'requirements.txt')
try:
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Pavel")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Orlov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("porlov@lanit.ru")
    file_button = browser.find_element_by_css_selector('[type="file"]')
    file_button.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(5)
finally:
    time.sleep(10)
    browser.quit()