from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    # считаем сумму
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    total = int(x) + int(y)

    # вводим данные
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(total))
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # копируем за 10сек и закрываем браузер
    time.sleep(10)
    browser.quit()

# пустая строка
