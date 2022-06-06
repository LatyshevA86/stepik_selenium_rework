from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from math import log, sin

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    # решаем уравнение
    x = browser.find_element(By.ID, 'input_value').text
    value = log(abs(12 * sin(int(x)))) 

    # вводим данные и скролим
    input1 = browser.find_element(By.ID, 'answer').send_keys(str(value))
    input2 = browser.find_element(By.ID, 'robotCheckbox').click()
    browser.execute_script("window.scrollBy(0, 150);")
    input3 = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ожидание и закрытие браузера
    time.sleep(10)
    browser.quit()

# пустая строка
