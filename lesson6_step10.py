from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Pavel")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Orlov")
    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("porlov@lanit.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
