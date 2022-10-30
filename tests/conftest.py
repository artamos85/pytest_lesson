
import allure
import pytest
import requests
from django.middleware.csrf import _get_new_csrf_string


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address
        self.csrftoken = _get_new_csrf_string()

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)

    def post(self, path="/", params=None, data=None, cookies=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, params=params, data=data, cookies=cookies, headers=headers)


@pytest.fixture
def test_main():
    return ApiClient(base_address='http://127.0.0.1:8000/')


def _get_token(test_main):
    response = test_main.get('login', headers={'Cookie': f'csrftoken={test_main.csrftoken}'})
    index_start = response.text.find('csrfmiddlewaretoken')
    index_start = response.text.find('value', index_start)
    index_start = response.text.find('"', index_start) + 1
    index_end = response.text.find('"', index_start)
    return response.text[index_start:index_end]


@pytest.fixture
def get_token(test_main):
    return _get_token(test_main)


@pytest.fixture
def login_data(test_main):
    csrfmiddlewaretoken = test_main.csrftoken
    acc_data = {
        'username': "admin",
        'password': "admin",
        'csrfmiddlewaretoken': csrfmiddlewaretoken
    }
    return acc_data