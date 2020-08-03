from framework.common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import LinkOperations, ElementOperations
from pageObjects.pages import MainPage, TicketsPage
import pytest

logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")

@pytest.mark.usefixtures("get_driver")
class TestSuite1:

    def test_one(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        MainPage.MainPage().findTickets()
        TicketsPage.Ticketspage().findTickets()





