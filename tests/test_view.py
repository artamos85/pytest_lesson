import allure

from django.middleware.csrf import _get_new_csrf_string

from shop.models import Product

OK_STATUS_CODE = 200


@allure.feature('Тест на отображение')
@allure.story('На главной странице последние 5 объектов из БД')
def test_main_page(test_main):
    token = _get_new_csrf_string()
    response = test_main.get('', headers={'Cookie': f'csrftoken={test_main.csrftoken}'})

    index = response.text.find('<div class="card">')
    count = 0
    while index > 0:
        count += 1
        index += 1
        index = response.text.find('<div class="card">', index)

    with allure.step('Подсчет числа продуктов'):
        assert count == 5, f"Всего {count} продуктов"


@allure.feature('Тест на отображение')
@allure.story('На странице с объектами находятся все объекты из БД')
def test_service_page(test_main):
    token = _get_new_csrf_string()
    response = test_main.get('service', headers={'Cookie': f'csrftoken={test_main.csrftoken}'})

    index = response.text.find('<div class="card">')
    count = 0
    while index > 0:
        count += 1
        index += 1
        index = response.text.find('<div class="card">', index)

    with allure.step('Подсчет числа продуктов'):
        assert count == 13, f"Всего {count} продуктов"