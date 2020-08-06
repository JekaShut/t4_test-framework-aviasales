from framework.utils.BaseElement import *



class Button(BaseElement):

    def click(self):
        '''
        :return: nothing
        Find and click to element
        '''
        self._find()
        self.element.click()

    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        return self.element.text

class Input(BaseElement):
    def click(self):
        '''
        :return: nothing
        Find and click to element
        '''
        self._find()
        self.element.click()

    def clear(self):
        '''
        :return: nothing
        Clear input textfield
        '''
        self._find()
        self.element.clear()

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self._find()
        self.element.send_keys(keys)


class Label(BaseElement):
    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        return self.element.text


class OneElement(BaseElement):
    def find(self):
        '''
        :return: one element
        '''
        return self._find()



class ManyElements(BaseElement):
    def find(self):
        '''
        :return: Many elements
        '''
        return self._finds()


class Element(BaseElement):
    def click(self):
        '''
        :return: nothing
        Find element in element and click it
        '''
        self.element.click()

    def getText(self):
        '''
        :return: element text
        '''
        self._find()
        return self.element.text





