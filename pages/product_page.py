from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        '''Клик по кнопке добавления товара в корзину'''
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_success_message(self):
        '''Проверка, что появилось сообщение об успешном добавлении в корзину'''
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET), \
            f'ОШИБКА! Не появилось сообщение об успешном добавлении в корзину'

    def should_not_be_success_message(self):
        '''Проверка, что нет сообщения об успешном добавлении в корзину'''
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET), \
            f'ОШИБКА! Не должно быть сообщения об успешном добавлении в корзину'

    def should_be_disappear_success_message(self):
        '''Проверка, что сообщение об успехе исчезает со страницы'''
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET), \
            "ОШИБКА! Сообщение об успехе не исчезло, но должно."

    def assert_product_name_in_success_message(self):
        '''Проверка, что название продукта в сообщении совпадает с названием товара на странице'''
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == product_name_message, \
            f'ОШИБКА! Ожидаемое имя продукта в сообщении: {product_name}, фактическое: {product_name_message}'

    def assert_product_price_in_basket_mini(self):
        '''Проверка, что цена товара совпадает с суммой в мини-корзине'''
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_mini_text = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        basket_mini_price = self.parse_basket_mini_total(basket_mini_text)
        assert product_price == basket_mini_price, \
            f'ОШИБКА! Ожидаемая сумма в корзине: {product_price}, фактическая: {basket_mini_price}'

    def parse_basket_mini_total(self, text):
        '''Извлекает сумму из строки мини корзины'''
        try:
            line_with_value = text.splitlines()[0]
            value = line_with_value.split(':', 1)[1].strip()
            return value
        except (IndexError, ValueError):
            return ''
