from ...component_base import ComponentBase
from .user_menu_popup_component import UserMenuPopupComponent
from selenium.common.exceptions import TimeoutException

class LoginMenuComponent(ComponentBase):

    def get_user_menu_popup(self):
        return UserMenuPopupComponent(self.driver)

    @property
    def is_authenticated(self):
        try:
            return bool(self.get_deferred_element_by_selector(self.get_locator('header.login_menu.user_menu'), timeout=5))
        except TimeoutException:
            return False

    @property
    def __user_area(self):
        return self.get_deferred_element_by_selector(self.get_locator('header.login_menu.user_area'))

    @property
    def __login_area(self):
        return self.get_deferred_element_by_selector(self.get_locator('header.login_menu.login_area'))
