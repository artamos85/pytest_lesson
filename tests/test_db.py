import allure

from shop.models import Product, User, Order


def del_user(username):
    try:
        u = User.objects.get(username = username)
        u.delete()

    except User.DoesNotExist:
        print("User doesnot exist")

@allure.feature('Работа с БД')
@allure.story('Создание пользователя')
def test_create_user():
    del_user('user_test')
    user = User.objects.create_user(username='user_test', email='user@test.kz',
                               password='41395e829c2895bda6d1407a410c6a3b3c3d806371b76879e1aa7ef377552ae8',
                               image='avatars/kreed7.jpg')
    assert user.username == 'user_test'


@allure.feature('Работа с БД')
@allure.story('Проверка созданного пользователя')
def test_get_user():
    user = User.objects.get(username='user_test')
    assert user.username == 'user_test'
    people = User.objects.all()
    assert people[0].id == 1

    del_user(user.username)




@allure.feature('Работа с БД')
@allure.story('Проверка продукта')
def test_get_product():
    product = Product.objects.create(title='product1', description='description product1', image='avatars/kreed7.jpg')
    assert product.title == 'product1'
    products = Product.objects.all()
    assert products[0].title == 'product1'


@allure.feature('Работа с БД')
@allure.story('Создаем заказ')
def test_create_product():
    del_user('user_tst')
    user = User.objects.create_user(username='user_tst', email='user@test.kz',
                                    password='41395e829c2895bda6d1407a410c6a3b3c3d806371b76879e1aa7ef377552ae8',
                                    image='avatars/kreed7.jpg')
    assert user.username == 'user_tst'
    _user = User.objects.get(id=1)

    product = Product.objects.create(title='product1', description='description product1', image='avatars/kreed7.jpg')
    assert product.title == 'product1'
    last_id = len(Product.objects.all())
    _product = Product.objects.get(last_id)

    order = Order.objects.create(user=_user, product=_product)
    assert order.id == 1
    orders = Order.objects.all()
    last_id = len(Order.objects.all())
    assert orders[last_id].id == last_id
