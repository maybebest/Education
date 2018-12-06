"""Pytest fixture for pywinauto app"""

import pytest
from .providers import DriverFactory, ConfigProvider
from . import App

TEST_CONFIG = ConfigProvider().get_config('config.txt')
APP_PATH = TEST_CONFIG.get_param('app_path')

# @pytest.yield_fixture(scope="function", params=[DriverFactory.get_chrome_driver,
#                                                 DriverFactory.get_firefox_driver])
@pytest.yield_fixture(scope="function", params=[DriverFactory.get_chrome_driver])
def driver(request):
    """driver fixture"""
    driver = request.param()
    driver.get(APP_PATH)
    yield driver
    driver.close()

@pytest.fixture(scope="function")
def app(driver):
    """driver fixture"""
    return App(driver)