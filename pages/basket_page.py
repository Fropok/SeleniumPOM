from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        '''Проверка на корректный url адрес страницы корзины'''
        current_url = self.browser.current_url
        assert 'basket' in current_url, f'ОШИБКА! Ожидаемый URL: страница логина, фактический URL: {current_url}'

    def should_be_basket_is_empty(self):
        '''Проверка, что появилось сообщение "Ваша корзина пуста"'''
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET), \
            f'ОШИБКА! Не появилось сообщение "Ваша корзина пуста"'

    def should_not_be_basket_items(self):
        '''Проверка, что нет предметов в корзине'''
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            f'ОШИБКА! Не должно быть предметов в корзине'
