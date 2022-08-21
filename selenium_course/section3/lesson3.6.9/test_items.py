from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_is_displayed(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    assert button.is_displayed() is True, 'Кнопка добавления в корзину не видна'


