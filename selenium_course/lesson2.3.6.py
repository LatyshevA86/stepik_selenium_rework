import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # переключаемся на новое окно и решаем уравнение
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value').text
    value = log(abs(12 * sin(int(x))))

    # вводим данные
    browser.find_element(By.ID, 'answer').send_keys(str(value))
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ожидаем и закрываем браузер
    time.sleep(10)
    browser.quit()

# пустая строка
