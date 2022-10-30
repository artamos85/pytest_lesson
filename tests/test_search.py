import allure

OK_STATUS_CODE = 200


@allure.feature('Тесты на поиска')
@allure.story('Переход на страницу выдачи результата')
def test_search_page(test_main, get_token):
    token = get_token
    response = test_main.get(f'search_result?csrfmiddlewaretoken={token}&search=1',
                             headers={'Cookie': f'csrftoken={test_main.csrftoken}'})
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"


@allure.feature('Тест на поиск')
@allure.story('Проверка возвращаемых значений')
def test_search_result(test_main, get_token):
    token = get_token
    response = test_main.get(f'search_result?csrfmiddlewaretoken={token}&search=1',
                             headers={'Cookie': f'csrftoken={test_main.csrftoken}'})
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"
        assert response.text.find('<div class="card">') > 0, "Продукты не найдены"