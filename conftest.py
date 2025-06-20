import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Select language: uk, ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, zh-hans, sk")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

# pytest -v --tb=line --language=en test_main_page.py
