import time
import pytest
from PageObject_Selenium_Python.pages.base_page import BasePage
from PageObject_Selenium_Python.pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_product(self, browser):
        # self.should_be_newYear_url(browser) в третьем задании не нужно
        self.should_be_add_to_basket_button()
        self.click_add_to_basket()

    def should_be_newYear_url(self, browser):
            # проверка на корректный url адрес (подстрока "?promo=newYear" есть в текущем url браузера)
        assert "?promo=newYear" in browser.current_url, "Не корректный url адрес"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON_LOCATOR), "ADD_TO_BASKET_BUTTON is not presented"

    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_LOCATOR)
            # Нажимаем кнопку Add to basket
        add_to_basket_button.click()

    def return_product_name(self, browser):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOCATOR).text
        return product_name

    def return_price(self, browser):
        price = self.browser.find_element(*ProductPageLocators.PRICE_LOCATOR).text
        return price

    def should_be_same_product_name(self, product_name):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_LOCATOR).text
        assert product_name == added_product_name, \
            f'Product name in catalog is "{product_name}" but in message is "{added_product_name}"'
        time.sleep(1)

    def should_be_same_price(self, price):
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_LOCATOR).text
        assert price == basket_value, f'The price is "{price}" but the basket value is "{basket_value}"'
        time.sleep(1)

        # метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

        # проверить, что элемент исчезает
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeared"
