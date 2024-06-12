from PageObject_Selenium_Python.pages.base_page import BasePage
from PageObject_Selenium_Python.pages.product_page import ProductPageLocators
from PageObject_Selenium_Python.pages.locators import BasketPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def basket_is_empty(self, browser):
        basket_is_empty_text = WebDriverWait(self.browser, 5). \
            until(EC.presence_of_element_located(BasketPageLocator.BASKET_IS_EMPTY_LOCATOR)).text
            # Ожидаем, что есть текст о том, что корзина пуста
        assert basket_is_empty_text == 'Your basket is empty. Continue shopping', \
            f'Your basket contains {basket_is_empty_text}, but should be "Your basket is empty. Continue shopping"'

    def should_not_be_product_in_basket(self):
            # Ожидаем, что в корзине нет товаров - сообщение об успешном добавлении отсуствует
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
