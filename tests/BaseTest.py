from common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import LinkOperations

logger = Logger(logger="BaseTest").getlog()

LOCAL = jsonGetter.GetJson.getConfig("LOCAL")
SITE = jsonGetter.GetJson.getConfig("SITE")
actualBrowser = jsonGetter.GetJson.getConfig("actualBrowser")

logger.info("\n" + "Browser : " + actualBrowser + "\n" + "Language is: " + LOCAL)


class TestRunbrowser():
    def test_runbrowser(self):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.OpenLink(SITE)


