from framework.logger.logger import Logger
from framework.utils import ElementOperations
from pageObjects.pages.logic import TicketPageLogic
from pageObjects.pages.logic import MainPageLogic
import time
import re

logger = Logger(logger="MainPage").getlog()


class Ticketspage:
    def __init__(self):
        self.TicketTextXpath = "//span[@class='buy-button__price']/span[@data-testid='price-with-logic']"
        self.StraightTextXpath = "//span[text()='Прямой']"
        self.BagageXpath = "//div[@class='filters__item filter --baggage']"
        self.BagageOpenedAll = "//label[@for='baggage_all']"
        self.FullBagageXpath = "//label[@for='baggage_full_baggage']"

    def findTickets(self, position=0):
        tickets = ElementOperations.ManyElements(locatorType="Xpath", locator=self.TicketTextXpath).find()
        lowestPrice = TicketPageLogic.logic().checkValues(tickets)
        return tickets[position], lowestPrice

    def findStraightPath(self):
        ElementOperations.Button(locatorType="Xpath", locator=self.StraightTextXpath).click()


    def setBagage(self):
        ElementOperations.Button(locatorType="Xpath", locator=self.BagageXpath).click()
        ElementOperations.Button(locatorType="Xpath", locator=self.BagageOpenedAll).click()
        ElementOperations.Button(locatorType="Xpath", locator=self.FullBagageXpath).click()



