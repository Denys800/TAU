import pytest
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from config.config import TestData
from config import config
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixture('browser')
class BasePage(TestData):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.BASE_URL

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, by_locator, time=config.TestData.EXPLICITLY_TIME):
        try:
            element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(by_locator))
            return element
        except TimeoutException:
            print(f"Can't find element by locator {by_locator}")

    def find_elements(self, by_locator, time=10):
        try:
            elements = WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(by_locator))
            return elements
        except TimeoutException:
            print(f"Can't find elements by locator {by_locator}")

    def send_keys(self, by_locator, text):
        input_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        input_text.send_keys(text)

    def click_element(self, by_locator, time=config.TestData.EXPLICITLY_TIME):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(by_locator), message=
        f"Can't find element by locator {by_locator}")
        element.click()

    def get_title(self):
        return self.driver.title

    def get_text(self, by_locator, time=config.TestData.EXPLICITLY_TIME):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(by_locator), message=
        f"Can't find element by locator {by_locator}")
        return element.text

    def element_is_visible(self, by_locator, time=config.TestData.EXPLICITLY_TIME):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    def dropdown_select(self, by_locator, value):
        dropdown = Select(self.find_element(by_locator))
        dropdown.select_by_value(value)

    @staticmethod
    def formating_list(lists):
        return [float(s.lstrip("$")) for s in lists]

