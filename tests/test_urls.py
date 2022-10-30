import pytest
import allure

OK_STATUS_CODE = 200


@allure.feature('Страницы открываются')
@allure.story('Получение страницы')
@pytest.mark.parametrize("input_param", [
    "",
    "login",
    "register",
    "profile",
    "service",
    "service/1",
    "admin"
])
def test_get_home(input_param, test_main):
    response = test_main.get(input_param)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"