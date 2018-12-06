"""Selenium WebDriver. Waitings"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

from .. providers import ConfigProvider

class ComponentBase(object):
    def __init__(self, driver: webdriver):
        self.driver = driver        

    def get_deferred_element_by_selector(self, selector, by=By.CSS_SELECTOR, timeout=120):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(
                (by, selector))
        )

    def wait_for_visibility_of_element(self, selector, by=By.CSS_SELECTOR, timeout=120):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                (by, selector))
        )

    def get_element_by_css_selector(self, css_selector, driver=None):
        driver = self.driver if not driver else driver
        elements = driver.find_elements_by_css_selector(css_selector)
        return elements[0] if len(elements) else None

    def get_locator(self, locator_path):
        return self.__get_locators_config().get_param(locator_path)

    def script_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @property
    def app_path(self):
        return self.__get_config().get_param('app_path')
    
    def __get_config(self):
        return ConfigProvider().get_config('config.txt')

    def __get_locators_config(self):
        return ConfigProvider().get_config('locators.txt')

