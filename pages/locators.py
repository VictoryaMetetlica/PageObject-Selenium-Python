class MainPageLocators():
        # переменная для логин-локатора
    LOGIN_LINK = ('css selector', "#login_link")


class LoginPageLocators():
    LOGIN_FORM = ('css selector', "#login_form")
    REGISTER_FORM = ('css selector', "#register_form")
    EMAIL_FIELD_LOCATOR = ('css selector', '#id_login-username')
    PASSWORD_FIELD_LOCATOR = ('css selector', '#id_login-password')
    LOG_IN_BUTTON_LOCATOR = ('css selector', '#login_form > button:nth-child(7)')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON_LOCATOR = ('css selector', '.btn-add-to-basket')
    PRODUCT_NAME_LOCATOR = ('css selector', '.product_main h1')
    ADDED_PRODUCT_NAME_LOCATOR = ('css selector', '.alertinner strong')
    PRICE_LOCATOR = ('css selector', 'p.price_color')
    BASKET_VALUE_LOCATOR = ('css selector', '.alertinner p strong')
    SUCCESS_MESSAGE = ('css selector', 'alert-success')

class BasePageLocators():
    LOGIN_LINK = ('css selector', "#login_link")
    LOGIN_LINK_INVALID = ('css selector', "#login_link_inc")
    VIEW_BASKET_BUTTON_MAIN_PAGE_LOCATOR = ('css selector', "span a.btn.btn-default")
    USER_ICON = ('css selector', ".icon-user")

class BasketPageLocator():
    BASKET_IS_EMPTY_LOCATOR = ('css selector', '#content_inner > p:nth-child(1)')