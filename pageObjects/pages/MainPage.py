from framework.logger.logger import Logger
from framework.utils import ElementOperations
from pageObjects.pages.logic import MainPageLogic
import time

logger = Logger(logger="MainPage").getlog()


class MainPage:
    def __init__(self):
        self.InNewPageXpath = "//label[@class='of_input_checkbox__label']"
        self.FromXpath = "//input[@placeholder='Откуда']"
        self.FromText = "Минск"
        self.ToXpath = "//input[@placeholder='Куда']"
        self.ToText = "Стамбул"
        self.ThereXpath = "//div[@class='trip-duration__input-wrapper --departure']"
        self.ValueToXpath = "//input[@class='trip-duration__date-input --active']"
        self.FromThereXpath = "//div[@class='trip-duration__input-wrapper --return']"
        self.openBookingXpath = "//label[@class='of_input_checkbox__label']"
        self.BackTicketXpath = "//div[@class='trip-duration__content-head']/button"
        self.ConfirmXpath = "//span[@class='form-submit__plane']"
        self.CalendarDayXpath = "//div[@class='calendar__day-cell ']"
        self.CalendarDayToodayXpath = "//div[@class='calendar__day-cell today']"
        self.PassiveInputDateXpath1 = "//div[1]/div/input[@class='trip-duration__date-input']"

    def sendKeys(self):

        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).send(self.ToText)
        # тут сделать нажатие на кнопку

        ElementOperations.Input(locatorType="Xpath", locator=self.openBookingXpath).click()
        ElementOperations.Button(locatorType="Xpath", locator=self.ThereXpath).click()

        day = MainPageLogic.logic().chooseRandomDate()
        ElementOperations.Element(element=day).click()

        #ElementOperations.Input(locatorType="Xpath", locator=self.PassiveInputDateXpath1)
        ElementOperations.Button(locatorType="Xpath", locator=self.FromThereXpath).click()
        ElementOperations.Button(locatorType="Xpath", locator=self.BackTicketXpath).click()
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).send(self.FromText)
        ElementOperations.Button(locatorType="Xpath", locator=self.ConfirmXpath).click()            # CONFIRM
        time.sleep(4)


