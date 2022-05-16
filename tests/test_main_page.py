import time

import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import config


class MainMenuTest:
    def test_main_menu_list(self, browser):
        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD
        expected_menu_list = config.TestData.EXPECTED_MENU_LIST

        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        login_page.log_in_user(USER_NAME, PASSWORD)
        main_page.click_main_menu_icon()
        actual_menu_list = main_page.get_main_menu()
        assert actual_menu_list == expected_menu_list


class SortingTest:
    def test_sorting_list(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        expected_dropdown_options = config.TestData.EXPECTED_DROPDOWN_OPTION
        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD
        login_page.log_in_user(USER_NAME, PASSWORD)
        actual_dropdown_options = main_page.get_list_options_drop_down()
        print(main_page.get_value_of_drop_down())
        assert actual_dropdown_options == expected_dropdown_options

    def test_switching_filter_option(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD

        login_page.log_in_user(USER_NAME, PASSWORD)
        main_page.choose_option(sort_by_value='lohi')
        time.sleep(1)
        main_page.choose_option(sort_by_value='hilo')
        time.sleep(1)
        main_page.choose_option(sort_by_value='za')
        time.sleep(1)
        main_page.choose_option(sort_by_value='az')

    def test_sorting_product_items_by_price(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD

        # sorting by price from low to high
        login_page.log_in_user(USER_NAME, PASSWORD)
        actual_sorted_price_of_items_lo_to_hi = sorted(main_page.get_price_of_product())
        print(actual_sorted_price_of_items_lo_to_hi)
        main_page.choose_option(sort_by_value='lohi')
        expected_sorted_price_of_items_lo_to_hi = main_page.get_price_of_product()
        print(expected_sorted_price_of_items_lo_to_hi)
        assert actual_sorted_price_of_items_lo_to_hi == expected_sorted_price_of_items_lo_to_hi

        # sorting by price from high to low
        actual_sorted_price_of_items_hi_to_lo = sorted(main_page.get_price_of_product(), reverse=True)
        print(actual_sorted_price_of_items_hi_to_lo)
        main_page.choose_option(sort_by_value='hilo')
        expected_sorted_price_of_items_hi_to_lo = main_page.get_price_of_product()
        print(expected_sorted_price_of_items_hi_to_lo)
        assert actual_sorted_price_of_items_hi_to_lo == expected_sorted_price_of_items_hi_to_lo

    def test_sorting_product_items_by_name(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD

        login_page.log_in_user(USER_NAME, PASSWORD)
        actual_sorted_name_of_items_Z_to_A = sorted(main_page.get_name_of_product(), reverse=True)
        main_page.choose_option(sort_by_value='za')
        print(actual_sorted_name_of_items_Z_to_A)
        expected_sorted_name_of_items_Z_to_A = main_page.get_name_of_product()
        print(expected_sorted_name_of_items_Z_to_A)
        assert actual_sorted_name_of_items_Z_to_A == expected_sorted_name_of_items_Z_to_A

        actual_sorted_name_of_items_A_to_Z = sorted(main_page.get_name_of_product())
        main_page.choose_option(sort_by_value='az')
        expected_sorted_name_of_items_A_to_Z = main_page.get_name_of_product()

        assert actual_sorted_name_of_items_A_to_Z == expected_sorted_name_of_items_A_to_Z


class AddRemoveButtonTest:
    def test_click_add_remove_button(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        USER_NAME = config.TestData.USER_NAME
        PASSWORD = config.TestData.PASSWORD

        login_page.log_in_user(USER_NAME, PASSWORD)
        main_page.click_add_to_cart_button()
        assert main_page.visibility_of_remove_button() == True
        main_page.click_remove_item_button()
        assert main_page.visibility_of_add_to_cart_button() == True
