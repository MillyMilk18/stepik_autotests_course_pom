import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def pytest_addoption(parser):
    parser.addoption('--language', default='en')

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture()
def setup(browser):
    password = 'adFGD67HG0'
    email = str(time.time()) + "@fakemail.org"
    login = LoginPage(browser, link)
    login.open()
    login.go_to_login_page()
    login.register_new_user(email, password)
    login.should_be_authorized_user()