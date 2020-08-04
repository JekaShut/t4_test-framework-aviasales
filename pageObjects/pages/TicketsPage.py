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

    def findTickets(self):
        tickets = ElementOperations.ManyElements(locatorType="Xpath", locator=self.TicketTextXpath).find()
        lowestPrice = TicketPageLogic.logic().checkValues(tickets)
        return tickets[0], lowestPrice





        #for ticket in tickets:
        #    text = ticket.text
        #    pattern = "\\d+"
        #    price = re.findall(pattern, text)
        #    x.append([ticket, price])
        #x.sort(key=lambda x: x[1])
        #lowestPrice = x[0][1]