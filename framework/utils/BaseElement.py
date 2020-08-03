from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.Browser import *
from abc import ABC

WaitTime = jsonGetter.GetJson.getConfig("WaitTime")


class BaseElement(ABC):
    def __init__(self, locatorType="None", locator="None", link="None"):
        self.locatorType = locatorType
        self.locator = locator
        self.driver = RunBrowser().driver
        self.link = link

    def _find(self):
        wait = WebDriverWait(self.driver, WaitTime)
        if self.locatorType == "Xpath":
            wait.until(EC.presence_of_element_located((By.XPATH, self.locator)))
            self.element = self.driver.find_element_by_xpath(self.locator)
        if self.locatorType == "Id":
            wait.until(EC.presence_of_element_located((By.ID, self.locator)))
            self.element = self.driver.find_element_by_id(self.locator)
        if self.locatorType == "Class":
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.locator)))
            self.element = self.driver.find_element_by_class_name(self.locator)
        if self.locatorType == "Css":
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
            self.element = self.driver.find_element_by_css_selector(self.locator)