class MainPageLocators():
        # переменная для логин-локатора
    LOGIN_LINK = ('css selector', "#login_link")
        # переменная для адреса страницы
    link = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators():
    LOGIN_FORM = ('css selector', "#login_form")
    REGISTER_FORM = ('css selector', "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON_LOCATOR = ('css selector', '.btn-add-to-basket')
    PRODUCT_NAME_LOCATOR = ('css selector', '.product_main h1')
    ADDED_PRODUCT_NAME_LOCATOR = ('css selector', '.alertinner strong')
    PRICE_LOCATOR = ('css selector', 'p.price_color')
    BASKET_VALUE_LOCATOR = ('css selector', '.alertinner p strong')
    SUCCESS_MESSAGE = ('css selector', 'alert-success')

