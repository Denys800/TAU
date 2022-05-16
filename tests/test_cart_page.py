import time

import pytest
from pages.Cart_page import CartPage
from pages.login_page import LoginPage
from config import config
from pages.main_page import MainPage


class CartPageTest:
    def test_open_cart(self, browser):
        login_page = LoginPage(browser)
        cart_page = CartPage(browser)
        main_page = MainPage(browser)

        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD

        login_page.log_in_user(USER_NAME, PASSWORD)
        main_page.producrts_to_json()
        cart_page.go_to_cart_page()
        assert cart_page.check_current_url('https://www.saucedemo.com/cart.html')
