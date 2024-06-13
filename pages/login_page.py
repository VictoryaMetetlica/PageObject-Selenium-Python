import PageObject_Selenium_Python.pages.locators
from PageObject_Selenium_Python.pages.base_page import BasePage
from PageObject_Selenium_Python.pages.locators import LoginPageLocators
from PageObject_Selenium_Python.pages.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
            # проверка на корректный url адрес (подстрока "login" есть в текущем url браузера)
        assert "login" in browser.current_url,  "Не корректный url адрес"

    def should_be_login_form(self):
            # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
            # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_enter = WebDriverWait(self.browser, 5). \
            until(EC.presence_of_element_located(LoginPageLocators.EMAIL_REG_FIELD_LOCATOR))
        email_enter.send_keys(email)
        password1_enter = WebDriverWait(self.browser, 5). \
            until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_REG1_FIELD_LOCATOR))
        password1_enter.send_keys(password)
        password2_enter = WebDriverWait(self.browser, 5). \
            until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_REG2_FIELD_LOCATOR))
        password2_enter.send_keys(password)
        register_button = WebDriverWait(self.browser, 5). \
            until(EC.presence_of_element_located(LoginPageLocators.REGISTER_BUTTON_LOCATOR))
        register_button.click()
        time.sleep(5)



