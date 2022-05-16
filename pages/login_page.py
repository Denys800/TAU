import pytest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login-button')
    LOGIN_FORM = (By.ID, 'login_button_container')

    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.driver.get(self.base_url)

    def log_in_user(self, login, password):
        self.set_user_name(login)
        self.set_user_password(password)
        self.click_login_button()

    def set_user_name(self, login):
        user_name_filed = self.find_element(LoginPage.USER_NAME)
        user_name_filed.send_keys(login)

    def set_user_password(self, password):
        user_password_filed = self.find_element(LoginPage.PASSWORD)
        user_password_filed.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(LoginPage.LOGIN)
        login_button.click()

    def visibility_of_login_form(self):
        login_form = self.element_is_visible(self.LOGIN_FORM)
        return login_form

    def get_error_text(self):
        error_message = self.get_text(self.ERROR_MESSAGE)
        return error_message

