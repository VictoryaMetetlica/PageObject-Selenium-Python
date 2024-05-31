from selenium.common.exceptions import NoSuchElementException
# базовая страница (с вспомогательными методами для работы с драйвером), от которой наследуются остальные классы
class BasePage():

    # добавляем конструктор — метод, который вызывается, когда создаем объект. Он объявляется ключевым словом __init__
    # (параметры: экземпляр драйвера и url адрес). Внутри конструктора сохраняем эти данные как аттрибуты класса

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


        # добавим команду для неявного ожидания со значением по умолчанию в 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

        # реализуем метод is_element_present, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # добавим метод open. Он должен открывать нужную страницу в браузере, используя метод get(). open() может обращаться
    # к атрибутам класса: self.browser и self.url

    def open(self):
        self.browser.get(self.url)


