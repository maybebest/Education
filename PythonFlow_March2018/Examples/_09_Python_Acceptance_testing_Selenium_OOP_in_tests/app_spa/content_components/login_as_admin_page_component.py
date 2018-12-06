from .content_component_base import ContentComponetBase
from .home_page_component import HomePageComponent

class LoginAsAdminComponent(ContentComponetBase):
    def __init__(self, driver, navigate=True):
        super().__init__(driver, navigate)        

        self.__login_form = self.get_deferred_element_by_selector(self.get_locator('login_page.login_form'))
        self.__email = self.get_element_by_css_selector(self.get_locator('login_page.email_input'))
        self.__password = self.get_element_by_css_selector(self.get_locator('login_page.password_input'))        

    @property
    def route(self):
        return 'login-form'

    def login(self, user_name, password):
        self.__fill_login_form(user_name, password)
        self.__login_form.submit()
        return HomePageComponent(self.driver, navigate=False)

    def __fill_login_form(self, user_name, password):
        self.__email.clear()
        self.__email.send_keys(user_name)
        self.__password.clear()
        self.__password.send_keys(password.strip())