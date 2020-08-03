from framework.utils.BaseElement import *


class Link(BaseElement):
    def get(self):
        self.driver.get(self.link)
