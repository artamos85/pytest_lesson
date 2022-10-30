import allure

OK_STATUS_CODE = 200


@allure.feature('Проверка авторизации')
@allure.story('Вход с учетной записью администратора')
def test_login(test_main, login_data):
    response = test_main.post("login", data=login_data,
                              headers={'Cookie': f'csrftoken={test_main.csrftoken}',
                                       'Content-Type': 'application/x-www-form-urlencoded'})
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"


@allure.feature('Проверка авторизации')
@allure.story('Выход с учетной записи администратора')
def test_logout(test_main, login_data):
    response = test_main.post("login", data=login_data,
                              headers={'Cookie': f'csrftoken={test_main.csrftoken}',
                                       'Content-Type': 'application/x-www-form-urlencoded'})

    cookie = response.request.headers.get('Cookie')
    response = test_main.get('logout', headers={'Cookie': cookie})

    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == OK_STATUS_CODE, f"Неверный код ответа, получен {response.status_code}"