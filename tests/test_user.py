import pytest
import allure

OK_STATUS_CODE = 200


@allure.feature('Тесты пользователя')
@allure.story('Заказ продукта 1')
@pytest.mark.parametrize("input_param", [
    "service/1/order"
])
def test_get_order(input_param, test_main, login_data):
    response = test_main.post("login", data=login_data,
                              headers={'Cookie': f'csrftoken={test_main.csrftoken}',
                                       'Content-Type': 'application/x-www-form-urlencoded'})
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"

    cookie = response.request.headers.get('Cookie')
    response = test_main.get(input_param, headers={'Cookie': cookie})

    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"


@allure.feature('Тесты пользователя')
@allure.story('На странице пользователя отображаются заказы')
def test_profile(test_main, login_data):
    response = test_main.post("login", data=login_data,
                              headers={'Cookie': f'csrftoken={test_main.csrftoken}',
                                       'Content-Type': 'application/x-www-form-urlencoded'})

    cookie = response.request.headers.get('Cookie')
    response = test_main.get("profile", headers={'Cookie': cookie})
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"
        assert response.text.find('<div class="card">') > 0, "Заказы не найдены"