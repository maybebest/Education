"""Selenium WebDriver. DSL"""

from ..test_base import TestBase
from ... import App


class TestLoginMenu(TestBase):
    def test_login_as_admin(self, app: App):
        login_page = app.get_login_page()
        home_page = login_page.login(app.admin_email, app.admin_password)

        assert home_page.is_authenticated

    def test_log_out(self, app: App):
        login_page = app.get_login_page()
        home_page = login_page.login(app.admin_email, app.admin_password)

        assert home_page.is_authenticated

        user_menu_popup = home_page.login_menu.get_user_menu_popup()

        home_page = user_menu_popup.open().log_out()
        assert not home_page.is_authenticated

    def test_user_menu_popup_appear_after_login(self, app: App):
        login_page = app.get_login_page()
        home_page = login_page.login(app.admin_email, app.admin_password)

        user_menu_popup = home_page.login_menu.get_user_menu_popup()
        assert not user_menu_popup.is_opened

        user_menu_popup.open()

        assert user_menu_popup.is_opened

    def test_user_menu_popup_closed_after_navigate_to_account_page(self, app: App):
        login_page = app.get_login_page()
        home_page = login_page.login(app.admin_email, app.admin_password)
        
        account_page = home_page.login_menu.get_user_menu_popup().open().open_account_page()

        assert not account_page.login_menu.get_user_menu_popup().is_opened
