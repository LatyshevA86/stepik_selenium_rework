from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # ждем цену 100дол и кликаем на кнопку
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    # решаем уравнение, вводим значение и кликаем
    x = browser.find_element(By.ID, 'input_value').text
    value = log(abs(12*sin(int(x))))

    browser.find_element(By.ID, 'answer').send_keys(str(value))
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    browser.quit()
    
