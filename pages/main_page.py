# Page Object, который будет связан с главной страницей интернет-магазина.

from PageObject_Selenium_Python.pages.base_page import BasePage      # бывает относительный путь from .base_page
from PageObject_Selenium_Python.pages.locators import MainPageLocators
from PageObject_Selenium_Python.pages.login_page import LoginPage

        # создадим класс MainPage, сделав его наследником класса BasePage. Класс-предок в Python указывается в скобках
class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"