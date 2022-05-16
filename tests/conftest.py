import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name")
    parser.addoption("--options", default='gui')


@pytest.fixture(scope='class')
def path_to_driver(request):
    if request.config.getoption('browser_name') == 'chrome':
        return ChromeDriverManager().install()
    elif request.config.getoption('browser_name') == 'firefox':
        return GeckoDriverManager().install()


@pytest.fixture(scope='class')
def browser(request, path_to_driver):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument(request.config.getoption('options'))
        driver = webdriver.Chrome(executable_path=path_to_driver, options=chrome_option)
    elif browser_name == 'firefox':
        firefox_option = webdriver.FirefoxOptions()
        if request.config.getoption('options') == 'headless':
            firefox_option.headless = True
        driver = webdriver.Firefox(executable_path=path_to_driver, options=firefox_option)
    yield driver
    driver.quit()

