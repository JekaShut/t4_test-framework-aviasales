from framework.logger.logger import Logger
from framework.utils import ElementOperations
import time

logger = Logger(logger="MainPage").getlog()


class MainPage:
    def __init__(self):
        self.InNewPageXpath = "//label[@class='of_input_checkbox__label']"
        self.FromXpath = "//input[@placeholder='Откуда']"
        self.FromText = "Минск"
        self.ToXpath = "//input[@placeholder='Куда']"
        self.ToText = "Варшава"
        self.ThereXpath = "//div[@class='trip-duration__input-wrapper --departure']"
        self.ValueToXpath = "//input[@class='trip-duration__date-input --active']"
        self.ValueTo = "23.08.2020"
        self.FromThereXpath = "//div[@class='trip-duration__input-wrapper --return']"

    def sendKeys(self):
        time.sleep(3) #тут добавить wait
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).send(self.FromText)
        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).send(self.ToText)
        time.sleep(2)
        ElementOperations.Button(locatorType="Xpath", locator=self.ThereXpath).click()
        ElementOperations.Input(locatorType="Xpath", locator=self.ValueToXpath).send(self.ValueTo) # тут сделать нажатие на кнопку
        time.sleep(2)
        ElementOperations.Button(locatorType="Xpath", locator=self.FromThereXpath).click()
        time.sleep(2)


