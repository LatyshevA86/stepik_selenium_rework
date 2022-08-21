import pytest
from selenium.webdriver.common.by import By
import time
from math import log

link_list = [
		'https://stepik.org/lesson/236895/step/1',
		'https://stepik.org/lesson/236896/step/1',
		'https://stepik.org/lesson/236897/step/1',
		'https://stepik.org/lesson/236898/step/1',
		'https://stepik.org/lesson/236899/step/1',
		'https://stepik.org/lesson/236903/step/1',
		'https://stepik.org/lesson/236904/step/1',
		'https://stepik.org/lesson/236905/step/1'
	    ]

# переходим на страницу, решаем уравнение, вводим ответ, отправляем ответ, сравниваем с текстом подтверждения
@pytest.mark.parametrize('link', link_list)
def test_lesson3_solve_and_compare_answer(browser, link):
    browser.get(f'{link}')

    # !!! НЕОБХОДИМО !!!  правильное локальное время для нахождения переменной
    answer = log(int(time.time()))

    browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(answer))
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

    assert message == 'Correct!', 'Соберите ошибки в предложение и отправьте в качестве ответа на задание'
