# Task
# Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)
# (параметр "?promo=newYear", чтобы получить проверочный код)
# Нажимаем на кнопку "Добавить в корзину".
# *Посчитать результат математического выражения и ввести ответ.
# Ожидаемый результат: Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем
# товаром, который вы действительно добавили. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.

import time
from PageObject_Selenium_Python.pages.product_page import ProductPage
from PageObject_Selenium_Python.conftest import browser

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
        # Открываем страницу товара
    page.open()
    page.should_be_product_url(browser)
    page.should_be_add_to_basket_button()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_equal_price_and_basket_value()
    time.sleep(2)





