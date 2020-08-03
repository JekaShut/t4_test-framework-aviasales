from framework.utils.BaseElement import *


class Button(BaseElement):
    def click(self):

        self._find()
        self.element.click()

    def getText(self):
        self._find()
        return self.element.text


class TextBox(BaseElement):
    def click(self):
        self._find()
        self.element.click()

    def input(self, keys):
        self._find()
        self.element.send_keys(keys)



