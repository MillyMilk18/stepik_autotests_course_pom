import pytest
from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    @pytest.fixture(autouse=True)
    def setup(self):
        password = 'adFGD67HG0'
        email = str(time.time()) + "@fakemail.org"
        self.go_to_login_page()
        self.register_new_user(email, password)
        self.should_be_authorized_user()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_str = 'login'
        assert login_str in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_passs = self.browser.find_elements(*LoginPageLocators.REGISTRATION_PASSWORD)
        for i in range(len(input_passs)):
            input_passs(i).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN).click()
