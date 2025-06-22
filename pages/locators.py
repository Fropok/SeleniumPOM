from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.ID, 'login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')


class MainPageLocators:
    pass


class LoginPageLocators:
    AUTHORIZATION_FORM = (By.ID, 'login_form')
    AUTHORIZATION_EMAIL = (By.ID, 'id_login-username')
    AUTHORIZATION_PASSWORD = (By.ID, 'id_login-password')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_2 = (By.ID, 'id_registration-password2')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE_SUCCESS_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages .alert-success')
    MESSAGE_PRODUCT_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_MINI = (By.CSS_SELECTOR, '.basket-mini')


class BasketPageLocators:
    MESSAGE_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
