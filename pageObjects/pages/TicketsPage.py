from framework.logger.logger import Logger
from framework.utils import ElementOperations
from pageObjects.pages.logic import TicketPageLogic



logger = Logger(logger="TicketsPage").getlog()


class Ticketspage:
    def __init__(self):
        self.TicketTextXpath = "//span[@class='buy-button__price']/span[@data-testid='price-with-logic']"
        self.StraightTextXpath = "//span[text()='Прямой']" # TODO: мб плохой локатор// тут по другому не получается,
                                                        # разве что через индекс, но эта вкладка есть не на всех выдачах
        self.BagageXpath = "//div[@class='filters__item filter --baggage']"
        self.BagageOpenedAll = "//label[@for='baggage_all']"
        self.FullBagageXpath = "//label[@for='baggage_full_baggage']"
        self.BagageTitleTextXpath = "//div[@class='ticket-tariffs__title']"
        self.TicketOriginDateXpath = "//div[@class='segment-route__endpoint origin']/div[@class='segment-route__date']"
        self.loaderAnimationFinishedXpath = "//div[@class='loader__stripes --animation-finished --blue']"

    def waitLoad(self):
        logger.info("Waiting for all results load")
        ElementOperations.Button("Xpath", self.loaderAnimationFinishedXpath)._find()

    def findTickets(self):
        logger.info("Trying to find list of tickets text")
        tickets = ElementOperations.ManyElements(locatorType="Xpath", locator=self.TicketTextXpath).find()
        return tickets

    def findLowestPrice(self, tickets):
        logger.info("Trying to find lowest price")
        lowestPrice = TicketPageLogic.logic().checkValues(tickets)
        return lowestPrice

    def findDates(self):
        originDates = ElementOperations.ManyElements(locatorType="Xpath", locator=self.TicketOriginDateXpath).find()
        datesRE = TicketPageLogic.logic().onlyDay(originDates)
        return datesRE


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



