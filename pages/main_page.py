# here we describe main page
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


# cart
class MainPage(BasePage):
    CART = (By.XPATH, '//a[@class="shopping_cart_link"]')
    MAIN_MENU_ICON = (By.ID, 'react-burger-menu-btn')
    MAIN_MENU_LIST = (By.CLASS_NAME, 'menu-item')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    DROP_DOWN_LIST = (By.XPATH, "//select[@class='product_sort_container']/option")
    DROP_DOWN = (By.XPATH, "//select[@class='product_sort_container']")
    PRICE_OF_PRODUCT = (By.XPATH, "//div[@class='inventory_item_price']")
    NAME_OF_PRODUCT = (By.XPATH, "//div[@class='inventory_item_name']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_visibility_of_cart(self):
        cart = self.element_is_visible(MainPage.CART)
        if cart:
            print('Cart is Visible and you are login')
            return True
        else:
            print('You are not login')

    def click_main_menu_icon(self):
        self.click_element(self.MAIN_MENU_ICON)

    def get_main_menu(self):
        actual_list = []
        menu_texts = self.find_elements(self.MAIN_MENU_LIST)
        for menu_text in menu_texts:
            actual_list.append(menu_text.text)
        return actual_list

    def logout_user(self):
        self.click_main_menu_icon()
        logout_button = self.find_element(self.LOGOUT_BUTTON)
        logout_button.click()

    def get_list_options_drop_down(self):
        actual_dropdown_list = []
        dropdown_items = self.find_elements(self.DROP_DOWN_LIST)
        for dropdown_item in dropdown_items:
            actual_dropdown_list.append(dropdown_item.text)
        return actual_dropdown_list

    def get_value_of_drop_down(self):
        actual_dropdown_value = []
        dropdown_values = self.find_elements(self.DROP_DOWN_LIST)
        for dropdown_value in dropdown_values:
            actual_dropdown_value.append(dropdown_value.get_attribute('value'))
        return actual_dropdown_value

    def choose_option(self, sort_by_value):
        low_to_high = self.dropdown_select(self.DROP_DOWN, sort_by_value)

    def get_price_of_product(self):
        prices_of_product = self.find_elements(self.PRICE_OF_PRODUCT)
        not_formated_prices_list = [price.text for price in prices_of_product]
        formated_list = self.formating_list(not_formated_prices_list)
        return formated_list

    def get_name_of_product(self):
        names_of_product = self.find_elements(self.NAME_OF_PRODUCT)
        not_sorted_names_list = [name.text for name in names_of_product]
        return not_sorted_names_list
