"""Selenium WebDriver."""

from .test_base import TestBase
from .. import App


class TestApp(TestBase):
    def test_app_window_title(self, app: App):
        assert app.get_home_page().get_window_title() == 'Animal Rescue Kharkiv, Ukraine'
