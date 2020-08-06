from framework.utils.BaseElement import *


class Url(BaseElement):
    def get(self):
        '''
        :return: URL of current page
        '''
        return self.driver.current_url