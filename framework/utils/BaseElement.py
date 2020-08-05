from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from framework.logger.logger import Logger

logger = Logger(logger="BaseElement").getlog()

from framework.Browser import *
from abc import ABC

WaitTime = jsonGetter.GetJson.getConfig("WaitTime")


class BaseElement(ABC):
    def __init__(self, locatorType="None", locator="None", link="None", element="None"):
        self.locatorType = locatorType
        self.locator = locator
        self.driver = RunBrowser().driver
        self.link = link
        self.element = element

    def _find(self, WaitTime = WaitTime):
        wait = WebDriverWait(self.driver, WaitTime)
        if self.locatorType == "Xpath":
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.element = self.driver.find_element_by_xpath(self.locator)
            return self.element

        if self.locatorType == "Id":
            try:
                wait.until(EC.presence_of_element_located((By.ID, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.element = self.driver.find_element_by_id(self.locator)
            return self.element

        if self.locatorType == "Class":
            try:
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.element = self.driver.find_element_by_class_name(self.locator)
            return self.element

        if self.locatorType == "Css":
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.element = self.driver.find_element_by_css_selector(self.locator)
            return self.element



    def _finds(self, WaitTime = WaitTime):
        wait = WebDriverWait(self.driver, WaitTime)
        if self.locatorType == "Xpath":
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.elements = self.driver.find_elements_by_xpath(self.locator)
        if self.locatorType == "Id":
            try:
                wait.until(EC.presence_of_element_located((By.ID, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.elements = self.driver.find_elements_by_id(self.locator)
        if self.locatorType == "Class":
            try:
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.elements = self.driver.find_elements_by_class_name(self.locator)
        if self.locatorType == "Css":
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
            except TimeoutException:
                logger.warn("Cannot find such an element!" + self.locator)
            self.elements = self.driver.find_elements_by_css_selector(self.locator)
        return self.elements