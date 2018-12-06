from .content_component_base import ContentComponetBase

class AccountDetailsPageComponent(ContentComponetBase):
    @property
    def route(self):
        return 'user-info'