from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common import jsonGetter
from framework.Browser import *
from abc import ABC, abstractmethod

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
            self.element = self.driver.find_element_by_xpath(self.locator)
        if self.locatorType == "Id":
            self.element = self.driver.find_element_by_id(self.locator)
        if self.locatorType == "Class":
            self.element = self.driver.find_element_by_class_name(self.locator)
        if self.locatorType == "Css":
            self.element = self.driver.find_element_by_css_selector(self.locator)