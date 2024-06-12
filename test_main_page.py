import time
from PageObject_Selenium_Python.pages.main_page import MainPage
from PageObject_Selenium_Python.pages.login_page import LoginPage
from PageObject_Selenium_Python.pages.product_page import ProductPage
from PageObject_Selenium_Python.pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
            # открываем страницу
        page.open()
            # выполняем метод страницы - неявно переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page(browser)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_from_main()
    time.sleep(2)
    page.basket_is_empty(browser)
    page.should_not_be_product_in_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_from_main()
    time.sleep(2)
    page.basket_is_empty(browser)
    page.should_not_be_product_in_basket()
