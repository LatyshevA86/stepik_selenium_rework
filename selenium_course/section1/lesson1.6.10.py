from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем ОБЯЗАТЕЛЬНЫЕ поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    input2.send_keys('Ivanov')
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    input3.send_keys('Ivan@petrov.com')

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст, и записываем в переменную
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

# пустая строка
