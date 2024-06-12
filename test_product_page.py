# Task 1
# Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)
# (параметр "?promo=newYear", чтобы получить проверочный код)
# Нажимаем на кнопку "Добавить в корзину".
# *Посчитать результат математического выражения и ввести ответ.
# Ожидаемый результат: Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем
# товаром, который вы действительно добавили. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
# Task 2
# Чтобы тест был независимым от контента: Измените методы проверки таким образом, чтобы они принимали как аргумент
# название товара и цену товара. Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.
# Сделайте такой же метод для цены.
# Task 3
# Найти баг на странице из списка ссылок, пометить падающий тест как xfail или skip.


import time
import pytest
from PageObject_Selenium_Python.pages.base_page import BasePage
from PageObject_Selenium_Python.pages.product_page import ProductPage
from PageObject_Selenium_Python.pages.login_page import LoginPage
from PageObject_Selenium_Python.conftest import browser

    # фикстура с параметризацией
#@pytest.mark.parametrize('promo_offer', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])

class TestUserAddToBasketFromProductPage(BasePage):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + time.time())
        page.register_new_user(email, password)
        page = BasePage(browser, link)
        time.sleep(2)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
            # Открываем страницу товара
        page.open()
        page.should_add_product(browser)
            # вычисляем выражение и записываем его в алерт
        #page.solve_quiz_and_get_code()
            # сопоставляем название товара в каталоге и в сообщении
        page.should_be_same_product_name(page.return_product_name(browser))
        page.should_be_same_price(page.return_price(browser))
        time.sleep(1)
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
            # Открываем страницу товара
        page.open()
        page.should_add_product(browser)
            # вычисляем выражение и записываем его в алерт
        # page.solve_quiz_and_get_code()
        page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
        # Открываем страницу товара
    page.open()
    page.should_add_product(browser)
        # вычисляем выражение и записываем его в алерт
    #page.solve_quiz_and_get_code()
        # сопоставляем название товара в каталоге и в сообщении
    page.should_be_same_product_name(page.return_product_name(browser))
    page.should_be_same_price(page.return_price(browser))
    time.sleep(1)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
            # Открываем страницу товара
    page.open()
    page.should_add_product(browser)
            # вычисляем выражение и записываем его в алерт
        # page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

    # гость может перейти на страницу логина со страницы товара
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()



