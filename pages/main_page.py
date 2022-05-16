
import json
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    CART = (By.XPATH, '//a[@class="shopping_cart_link"]')
    MAIN_MENU_ICON = (By.ID, 'react-burger-menu-btn')
    MAIN_MENU_LIST = (By.CLASS_NAME, 'menu-item')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    DROP_DOWN_LIST = (By.XPATH, "//select[@class='product_sort_container']/option")
    DROP_DOWN = (By.XPATH, "//select[@class='product_sort_container']")
    PRICE_OF_PRODUCT = (By.XPATH, "//div[@class='inventory_item_price']")
    NAME_OF_PRODUCT = (By.XPATH, "//div[@class='inventory_item_name']")

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    REMOVE_ITEM_BUTTON = (By.XPATH, "//button[text()='Remove']")

    MAIN_P = (By.XPATH, "//div[@class = 'inventory_item']")

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

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def visibility_of_add_to_cart_button(self):
        remove_button = self.element_is_visible(self.ADD_TO_CART_BUTTON)
        return bool(remove_button)

    def click_remove_item_button(self):
        self.click_element(self.REMOVE_ITEM_BUTTON)

    def visibility_of_remove_button(self):
        remove_button = self.element_is_visible(self.REMOVE_ITEM_BUTTON)
        return bool(remove_button)

    # ------------------------------------------------------------------------------------------------------------------
    with open("data.json", "w") as f:
        json.dump([], f)

    def write_json(self, new_data, filename='data.json'):
        with open(filename, 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data.append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)

    def producrts_to_json(self):
        items = self.find_elements(self.MAIN_P)
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            description = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
            print("Name: " + name)
            print("Price: " + price)
            print("Description:" + description)

            self.write_json({
                "name": name,
                "price": price,
                "description": description

            })
