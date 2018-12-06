"""Selenium WebDriver"""

from selenium import webdriver
from . config_provider import ConfigProvider

test_config = ConfigProvider().get_config('config.txt')


class DriverFactory(object):

    @staticmethod
    def get_chrome_driver(driver_path=None):
        path = DriverFactory.__get_driver_path(
            driver_path, 'chrome_driver_path')
        return webdriver.Chrome(path) if path else webdriver.Chrome()

    @staticmethod
    def get_ie_driver(driver_path=None):
        path = DriverFactory.__get_driver_path(driver_path, 'ie_driver_path')
        return webdriver.Ie(path) if path else webdriver.Ie()

    @staticmethod
    def get_firefox_driver(driver_path=None):
        path = DriverFactory.__get_driver_path(
            driver_path, 'firefox_driver_path')
        return webdriver.Firefox(executable_path=path) if path else webdriver.Firefox()

    @staticmethod
    def __get_driver_path(custom_path, driver_path_var):
        if custom_path:
            return custom_path
        path = test_config.get_param(driver_path_var)
        return path.replace("\\", "\\\\") if path else None
