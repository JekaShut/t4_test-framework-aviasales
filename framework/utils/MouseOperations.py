from selenium.webdriver.common.action_chains import ActionChains
from framework.utils.BaseElement import *

BROWSER = jsonGetter.GetJson.getConfig("actualBrowser")


class Mouse(BaseElement):
    def move(self):
        self._find()
        hov = ActionChains(self.driver).move_to_element((self.element)).perform()
