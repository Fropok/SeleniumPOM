import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''Открываем браузер'''
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        '''Проверка присутствия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        '''Проверка отсутствия элемента на странице'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        '''Проверка, что элемент исчез со страницы в течение timeout секунд'''
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=1, ignored_exceptions=[TimeoutException]) \
                .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        '''Решить викторину и получить код для успешного добавления в корзину'''
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

    def parse_basket_mini_total(self, text):
        '''Извлекает сумму из строки мини корзины'''
        try:
            line_with_value = text.splitlines()[0]
            value = line_with_value.split(':', 1)[1].strip()
            return value
        except (IndexError, ValueError):
            return ''
