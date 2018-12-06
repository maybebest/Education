from ...component_base import ComponentBase

class UserMenuPopupComponent(ComponentBase):        
    def open(self):
        self.__user_menu.click()
        return self

    @property
    def is_opened(self):
        visible_popup_element = self.get_element_by_css_selector('%s.is-visible' % self.get_locator('header.login_menu.user_menu_popup'))
        return self.__user_menu and visible_popup_element

    def open_account_page(self):
        account_menu_item = self.get_element_by_css_selector(self.get_locator('header.login_menu.user_menu_popup_account'))
        self.script_click(account_menu_item)
        
        from ...content_components import AccountDetailsPageComponent
        return AccountDetailsPageComponent(self.driver)

    def log_out(self):
        log_out_menu_item = self.get_element_by_css_selector(self.get_locator('header.login_menu.user_menu_popup_log_out'))
        self.script_click(log_out_menu_item)
        self.get_deferred_element_by_selector(self.get_locator('header.login_menu.login_area'))
        from ...content_components import HomePageComponent
        return HomePageComponent(self.driver)

    @property
    def __user_menu(self):
        return self.get_deferred_element_by_selector(self.get_locator('header.login_menu.user_menu'))

    
   
            
