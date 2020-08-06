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

    def onlyDay(self, elems):
        x = []
        for date in elems:
            text = date.text
            pattern = r"\d+"
            day = re.findall(pattern, text)
            x.append(day[0])
        return x

