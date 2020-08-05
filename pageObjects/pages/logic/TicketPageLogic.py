from framework.utils import ElementOperations
import random
import re

class logic:
    def sortFunc(self, elem):
        text = elem.text
        pattern = r"\d"
        ticket = re.findall(pattern, text)
        ticket = "".join(ticket)
        return ticket

    def checkValues(self, tickets):
        tickets.sort(key=self.sortFunc)
        return tickets[0]

    def onlyDay(self, elem):
        text = elem.text
        pattern = r"\d+"
        day = re.findall(pattern, text)
        return day[0]

