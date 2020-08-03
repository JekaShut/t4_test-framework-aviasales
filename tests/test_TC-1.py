from common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import LinkOperations, UrlOperations
import time
logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")


class TestSteamDownload:

    def test_pageload(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.OpenLink(SITE)
        #assert SITE == GetUrl.Get().CurrentUrl()



