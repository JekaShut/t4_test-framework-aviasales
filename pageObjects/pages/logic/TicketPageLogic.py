from framework.utils import ElementOperations
import random
import re

class logic:
    def sortFunc(self, elem):
        text = elem.text
        pattern = "\d+\s?\d+?"
        ticket = re.findall(pattern, text)
        return ticket

    def checkValues(self, tickets):
        x = []
        for elem in tickets:
            text = elem.text
            pattern = "\\d+"
            ticket = re.findall(pattern, text)
            try:
                lastx = x[-1].text
                lastt = re.findall(pattern, lastx)
                if int(ticket) < int(lastt):
                    x.append(elem)
            except:
                x.append(elem)

        x.sort(key=self.sortFunc)
        return x[0]


