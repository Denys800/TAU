import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from config import config


@pytest.mark.parametrize('user_name, password, error_message',
                         [
                             ('wrong_name', 'wrong_pass',
                              'Epic sadface: Username and password do not match any user in this service'),
                             ('', 'wrong_pass', 'Epic sadface: Username is required'),
                             ('wrong_name', '', 'Epic sadface: Password is required')
                         ]
                         )
def test_login_with_wrong_credentials(browser, user_name, password, error_message):
    login_page = LoginPage(browser)
    login_page.set_user_name(login=user_name)
    login_page.set_user_password(password=password)
    login_page.click_login_button()
    assert login_page.get_error_text() == error_message


def test_login_logout(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)

    USER_NAME = config.TestData.USER_NAME
    PASSWORD = config.TestData.PASSWORD

    login_page.set_user_name(login=USER_NAME)
    login_page.set_user_password(password=PASSWORD)
    login_page.click_login_button()
    time.sleep(1)
    assert main_page.verify_visibility_of_cart() == True
    main_page.logout_user()
    assert login_page.visibility_of_login_form()
