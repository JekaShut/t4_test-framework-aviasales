from framework.utils.BaseElement import *


class Button(BaseElement):
    def click(self):

        self._find()
        self.element.click()

    def getText(self):
        self._find()
        return self.element.text



class Input(BaseElement):
    def click(self):
        self._find()
        self.element.click()

    def send(self, keys):
        self._find()
        self.element.send_keys(keys)


class Label(BaseElement):
    def getText(self):
        self._find()
        return self.element.text



