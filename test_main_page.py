import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
        # открываем страницу
    page.open()
        # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page()
    time.sleep(5)
    # login_link = browser.find_element('css selector', "#login_link")
    # login_link.click()
