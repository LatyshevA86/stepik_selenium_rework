from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from math import *

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    # ищем атрибут
    attr = browser.find_element(By.ID, 'treasure')
    attr_get = attr.get_attribute('valuex')

    # решаем уравнение
    x = attr_get
    value = log(abs(12 * sin(int(x))))

    # вводим данные
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(value))
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    input4 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    input4.click()

finally:
    # копируем за 10сек и закрываем браузер
    time.sleep(10)
    browser.quit()

# пустая строка
