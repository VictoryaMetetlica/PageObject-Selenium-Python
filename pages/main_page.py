# Page Object, который будет связан с главной страницей интернет-магазина.

from PageObject_Selenium_Python.pages.base_page import BasePage      # бывает относительный путь from .base_page
from PageObject_Selenium_Python.pages.locators import MainPageLocators
from PageObject_Selenium_Python.pages.login_page import LoginPage

        # создадим класс MainPage, сделав его наследником класса BasePage. Класс-предок в Python указывается в скобках
class MainPage(BasePage):
        # В классе MainPage не осталось никаких методов, поэтому добавим заглушку: метод __init__ вызывается при
        # создании объекта. Конструктор с ключевым словом super вызывает конструктор класса предка и передает ему
        # аргументы, которые мы передали в конструктор MainPage.
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)