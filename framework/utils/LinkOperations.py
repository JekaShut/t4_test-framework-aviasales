from framework.utils.BaseElement import *


class Link(BaseElement):
    def __init__(self, link="None"):
        self.driver = RunBrowser().driver
        self.link = link


    def get(self):
        self.driver.get(self.link)
