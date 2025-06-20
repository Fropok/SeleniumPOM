from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    AUTHORIZATION_FORM = (By.ID, 'login_form')
    AUTHORIZATION_EMAIL = (By.ID, 'id_login-username')
    AUTHORIZATION_PASSWORD = (By.ID, 'id_login-password')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_2 = (By.ID, 'id_registration-password2')
