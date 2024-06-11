import pytest
from PageObject_Selenium_Python.pages.product_page import ProductPage
from PageObject_Selenium_Python.conftest import browser
from .pages.locators import ProductPageLocators


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
        #Открываем страницу товара
    page.open()
        # Добавляем товар в корзину
    page.should_add_product(browser)
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
        # Открываем страницу товара
    page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
        #Открываем страницу товара
    page.open()
        # Добавляем товар в корзину
    page.should_add_product(browser)
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_disappeared_success_message()
