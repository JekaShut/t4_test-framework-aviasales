from framework.utils.BaseElement import *


class Link(BaseElement):
    def __init__(self, link="None"):
        '''
        :param link: Link to get
        '''
        self.driver = RunBrowser().driver
        self.link = link


    def get(self):
        '''
        Follow to link
        '''
        self.driver.get(self.link)
