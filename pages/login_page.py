from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        '''Проверка на корректный url адрес страницы логина'''
        current_url = self.browser.current_url
        assert 'login' in current_url, f'ОШИБКА! Ожидаемый URL: страница логина, фактический URL: {current_url}'

    def should_be_login_form(self):
        '''Проверка наличия формы регистрации на странице'''
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_FORM), 'ОШИБКА! Форма авторизации отсутствует'

    def should_be_register_form(self):
        '''Проверка наличия формы регистрации на странице'''
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'ОШИБКА! Форма регистрации отсутствует'
