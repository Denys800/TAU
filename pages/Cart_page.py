from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    Cart_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")

    def go_to_cart_page(self):
        cart_link = self.click_element(self.Cart_LINK)

    def check_current_url(self, expected_url):
        actual_url = self.get_current_url()
        try:
            if actual_url == expected_url:
                return True
        except AssertionError:
            return print(f'{actual_url} is not as {expected_url}')
