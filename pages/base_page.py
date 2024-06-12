from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject_Selenium_Python.pages.locators import BasePageLocators

# базовая страница (с вспомогательными методами для работы с драйвером), от которой наследуются остальные классы
class BasePage():

    # добавляем конструктор — метод, который вызывается, когда создаем объект. Он объявляется ключевым словом __init__
    # (параметры: экземпляр драйвера и url адрес). Внутри конструктора сохраняем эти данные как аттрибуты класса

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
            # добавим команду для неявного ожидания со значением по умолчанию в 10
        self.timeout = timeout                  # устанавливаем значение времени ожидания для атрибута объекта
        self.browser.implicitly_wait(timeout)

    def go_to_basket_from_main(self):
        view_basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON_MAIN_PAGE_LOCATOR)
        view_basket.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

         # реализуем метод is_element_present, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

        # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
            # Устанавливаем неявное ожидание на 0
        self.browser.implicitly_wait(0)

        try:
            # Теперь будет использоваться только таймер из явного ожидания
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        # Устанавливаем таймер обратно на значение указанное в конструкторе
        finally:
            self.browser.implicitly_wait(self.timeout)

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout, 1, TimeoutException).\
             until_not(EC.presence_of_element_located((how, what))))
        except TimeoutException:
            return False

        return True

    # добавим метод open. Он должен открывать нужную страницу в браузере, используя метод get(). open() может обращаться
    # к атрибутам класса: self.browser и self.url

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                         " probably unauthorised user"
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

        # Посчитать результат математического выражения для тестов в product_page.py для получения проверочного кода
    def solve_quiz_and_get_code(self) -> object:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")