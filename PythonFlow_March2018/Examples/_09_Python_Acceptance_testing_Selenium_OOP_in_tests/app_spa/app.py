from . content_components import HomePageComponent, LoginAsAdminComponent

from .. providers import ConfigProvider


class App(object):
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePageComponent(self.driver)

    def get_login_page(self):
        return LoginAsAdminComponent(self.driver)

    @property
    def admin_email(self):
        return self.__get_config().get_param('admin.email')

    @property
    def admin_password(self):
        return self.__get_config().get_param('admin.password')

    def __get_config(self):
        return ConfigProvider().get_config('test_data.txt')
