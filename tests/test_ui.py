import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from shop.models import User


chrome_driver = 'D:\Documents\Учеба\Обучение авто\pytest_lesson\chromedriver.exe'
path_to_photo = u"D:/Documents/Учеба/Обучение авто/pytest_lesson/avatars/kreed7.jpg"
username = 'test'
mail = 'test@tester.ru'
password = 'Ckj;ysq_Gfhjkkn1'
register_username_path = '/html/body/div/div/form/div[1]/div/div/input'
register_mail_path = '/html/body/div/div/form/div[2]/div/div/input'
register_photo_path = '/html/body/div/div/form/div[5]/div/div/input'
register_send_button_path = '/html/body/div/div/form/button'
login_username_path = '/html/body/div[1]/div/form/div[1]/div/div/input'
login_password_path = '/html/body/div[1]/div/form/div[2]/div/div/input'
login_button = '/html/body/div/div/form/button'
profile_username_path = '/html/body/div[1]/div/div/div[1]/div[2]/h5'


def del_user(user):
    try:
        u = User.objects.get(username=user)
        u.delete()
        with allure.step("Проверяем удаление пользователя"):
            assert u not in User.objects.all(), f"Пользователь не удален"
    except:
        print("User does not exist")


@allure.feature('Проверка логина')
@allure.story('Вход в учетную запись Админа')
def test_user_login():
    driven = webdriver.Chrome(executable_path=chrome_driver)
    driven.get("http://127.0.0.1:8080/login")
    driven.find_element(By.XPATH, login_username_path).send_keys('admin')
    driven.find_element(By.XPATH, login_password_path).send_keys('admin')
    driven.find_element(By.XPATH, login_button).click()
    driven.get("http://127.0.0.1:8080/profile")
    with allure.step("Проверяем произошел ли переход на окно входа"):
        assert driven.find_element(By.XPATH, profile_username_path).is_displayed(), f"Окно не открылось"


@allure.feature('Проверка регистрации')
@allure.story('Попытка создания пользователя')
def test_user_create():
    driven = webdriver.Chrome(executable_path=chrome_driver)
    driven.get("http://127.0.0.1:8080/register")
    driven.find_element(By.XPATH, register_username_path).send_keys(username)
    driven.find_element(By.XPATH, register_mail_path).send_keys(mail)
    driven.find_element(By.NAME, 'password1').send_keys(password)
    driven.find_element(By.NAME, 'password2').send_keys(password)
    driven.find_element(By.XPATH, register_mail_path).send_keys(path_to_photo)
    driven.find_element(By.XPATH, register_send_button_path).click()
    with allure.step("Проверяем произошел ли переход на окно входа"):
        assert driven.find_element(By.XPATH, '/html/body/div[1]/div/h2').is_displayed(), f"Окно не открылось"
    del_user("test")