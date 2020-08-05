from framework.logger.logger import Logger
from framework.utils import ElementOperations
from pageObjects.pages.logic import TicketPageLogic
from pageObjects.pages.logic import MainPageLogic
import time
import re

logger = Logger(logger="TicketsPage").getlog()


class Ticketspage:
    def __init__(self):
        self.TicketTextXpath = "//span[@class='buy-button__price']/span[@data-testid='price-with-logic']"
        self.StraightTextXpath = "//span[text()='Прямой']"
        self.BagageXpath = "//div[@class='filters__item filter --baggage']"
        self.BagageOpenedAll = "//label[@for='baggage_all']"
        self.FullBagageXpath = "//label[@for='baggage_full_baggage']"
        self.BagageTitleTextXpath = "//div[@class='ticket-tariffs__title']"

    def findTickets(self, position=0):
        logger.info("Trying to find list of tickets text")
        tickets = ElementOperations.ManyElements(locatorType="Xpath", locator=self.TicketTextXpath).find()
        logger.info("Trying to find lowest price")
        lowestPrice = TicketPageLogic.logic().checkValues(tickets)
        return tickets[position], lowestPrice

    def findStraightPath(self):
        logger.info("Trying to click 'Прямой' button")
        ElementOperations.Button(locatorType="Xpath", locator=self.StraightTextXpath).click()


    def setBagage(self):
        logger.info("Trying to open baggage dropdown in filters")
        ElementOperations.Button(locatorType="Xpath", locator=self.BagageXpath).click()
        logger.info("Trying to click ALL baggage checkbox")
        ElementOperations.Button(locatorType="Xpath", locator=self.BagageOpenedAll).click()
        logger.info("Trying to click full baggage checkbox")
        ElementOperations.Button(locatorType="Xpath", locator=self.FullBagageXpath).click()

        logger.info("Trying to find tickets")
        tickets = ElementOperations.ManyElements(locatorType="Xpath", locator=self.TicketTextXpath).find()
        logger.info("Trying to find tickets with baggage")
        withBagage = ElementOperations.ManyElements(locatorType="Xpath", locator=self.BagageTitleTextXpath).find()
        logger.info("Trying calculate tickets")
        lenTick = len(tickets)
        logger.info("Trying to calculate tickets with baggage")
        lenBagage = len(withBagage)
        return lenTick, lenBagage



