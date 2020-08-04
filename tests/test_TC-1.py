from framework.common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import LinkOperations, ElementOperations
from pageObjects.pages import MainPage, TicketsPage
import pytest
import time

logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")

@pytest.mark.usefixtures("get_driver")
class TestSuite1:

    def test_one(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        MainPage.MainPage().findTickets()
        lowest = TicketsPage.Ticketspage().findTickets(0)
        assert lowest[0] == lowest[1], "The cheapest element is not first"


    def test_two(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        MainPage.MainPage().findTickets()
        TicketsPage.Ticketspage().findStraightPath()
        lowest = TicketsPage.Ticketspage().findTickets(-1)
        assert lowest[0] == lowest[1], "The cheapest element is not last"
        pass


