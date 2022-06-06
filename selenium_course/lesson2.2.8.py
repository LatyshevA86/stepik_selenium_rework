import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    # вводим данные
    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('ivan@ivanov.com')

    # загружаем ЛОКАЛЬНЫЙ файл
    browser.find_element(By.ID, 'file').send_keys('/home/aleksei/file.txt')

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ждем 10 сек и закрываем браузер
    time.sleep(10)
    browser.quit()

# пустая строка
