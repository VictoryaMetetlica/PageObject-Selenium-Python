from PageObject_Selenium_Python.pages.base_page import BasePage
from PageObject_Selenium_Python.pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON_LOCATOR), "ADD_TO_BASKET_BUTTON is not presented"

    def should_be_product_url(self, browser):
        # проверка на корректный url адрес (подстрока "?promo=newYear" есть в текущем url браузера)
        assert "?promo=newYear" in browser.current_url, "Не корректный url адрес"

    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_LOCATOR)
            # Нажимаем кнопку Add to basket
        add_to_basket_button.click()

    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOCATOR).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_LOCATOR).text
        assert product_name == added_product_name, 'Product names in catalog and message are different'

    def should_equal_price_and_basket_value(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_LOCATOR).text
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_LOCATOR).text
        assert price == basket_value, 'The basket value does not match the product price'


