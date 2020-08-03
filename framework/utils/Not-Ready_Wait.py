from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.utils.BaseElement import *



class WaitXpathLocated:
    def __init__(self, Xpath, time):
        wait = WebDriverWait(RunBrowser().driver, time)
        element = wait.until(EC.presence_of_element_located(By.XPATH, Xpath))
