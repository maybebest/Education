"""Selenium WebDriver. Waitings"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('app')
class TestBase(object):
    pass    
