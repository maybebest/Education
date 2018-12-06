from .. component_base import ComponentBase
from .. header import NavigationMenu, LoginMenu, TranslationMenu

class ContentComponetBase(ComponentBase):
    def __init__(self, driver, navigate=True):
        super().__init__(driver)
        self.__login_menu = LoginMenu(self.driver)
        self.__navigation_menu = NavigationMenu(self.driver)
        self.__translation_menu = TranslationMenu(self.driver)
        if navigate:
            self.__navigate()

    @property
    def route(self):
        raise NotImplementedError('Route is not implemented yet for %s' % self.__class__)
    
    @property
    def is_authenticated(self):
        return self.login_menu.is_authenticated

    @property
    def login_menu(self):
        return self.__login_menu
    
    @property
    def navigation_menu(self):
        return self.__login_menu

    @property
    def translation_menu(self):
        return self.__login_menu

    def get_window_title(self):
        return self.driver.title

    def __navigate(self):
        return self.driver.get('%s%s' % (self.app_path, self.route))

    