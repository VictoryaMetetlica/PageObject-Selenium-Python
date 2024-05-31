# Page Object, который будет связан с главной страницей интернет-магазина.

from .base_page import BasePage      # в зависимости от пакетов может потребоваться точка from .base_page import BasePage

        # создадим класс MainPage, сделав его наследником класса BasePage. Класс-предок в Python указывается в скобках

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element('css selector', '#login_link')
        login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element('css selector', '#login_link'), "Login link is not presented"