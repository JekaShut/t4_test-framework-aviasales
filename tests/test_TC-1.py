from framework.common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import LinkOperations
import pytest

logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")

@pytest.mark.usefixtures("get_driver")
class TestSuite1:

    def test_one(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        #assert SITE == GetUrl.Get().CurrentUrl()

    def test_two(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        #assert SITE == GetUrl.Get().CurrentUrl()



