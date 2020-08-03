from framework.utils.BaseElement import *


class Url(BaseElement):
    def get(self):
        return self.driver.current_url