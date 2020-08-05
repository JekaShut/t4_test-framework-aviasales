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

    def clear(self):
        self._find()
        self.element.clear()

    def send(self, keys):
        self._find()
        self.element.send_keys(keys)


class Label(BaseElement):
    def getText(self):
        self._find()
        return self.element.text


class OneElement(BaseElement):
    def find(self):
        return self._find()



class ManyElements(BaseElement):
    def find(self):
        return self._finds()


class Element(BaseElement):
    def click(self):
        self.element.click()

    def getText(self):
        self._find()
        return self.element.text

    #def find(self):
    #    self.element.



