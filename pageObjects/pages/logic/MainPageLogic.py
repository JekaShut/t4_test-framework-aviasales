from framework.utils import ElementOperations
import random

class logic:
    def __init__(self):
        self.CalendarDayXpath = "//div[@class='calendar__day-cell ']"
        self.CalendarDayToodayXpath = "//div[@class='calendar__day-cell today']"
    def chooseRandomDate(self):
        today = ElementOperations.OneElement(locatorType="Xpath", locator=self.CalendarDayToodayXpath).find()
        days = ElementOperations.ManyElements(locatorType="Xpath", locator=self.CalendarDayXpath).find()
        days.append(today)
        day = random.choice(days)
        return day