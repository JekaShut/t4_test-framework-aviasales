from framework.logger.logger import Logger
from framework.utils import ElementOperations
from pageObjects.pages.logic import MainPageLogic
from framework.utils.BaseElement import Keys
import time
import pytest


logger = Logger(logger="MainPage").getlog()


class MainPage:
    def __init__(self):
        self.InNewPageXpath = "//label[@class='of_input_checkbox__label']"
        self.FromXpath = "//input[@placeholder='Откуда']"
        self.ToXpath = "//input[@placeholder='Куда']"
        self.ThereXpath = "//div[@class='trip-duration__input-wrapper --departure']"
        self.ValueToXpath = "//input[@class='trip-duration__date-input --active']"
        self.FromThereXpath = "//div[@class='trip-duration__input-wrapper --return']"
        self.openBookingXpath = "//label[@class='of_input_checkbox__label']"
        self.BackTicketXpath = "//div[@class='trip-duration__content-head']/button"
        self.ConfirmXpath = "//span[@class='form-submit__plane']"
        self.CalendarDayXpath = "//div[@class='calendar__day-cell ']"
        self.CalendarDayToodayXpath = "//div[@class='calendar__day-cell today']"
        self.PassiveInputDateXpath1 = "//div[1]/div/input[@class='trip-duration__date-input']"
        self.DropdownXpath = "//div[@class='autocomplete__dropdown']/section"


    def findTickets(self, fromC, toC):
        ElementOperations.Input(locatorType="Xpath", locator=self.openBookingXpath).click()  # Remove checkbox
        ElementOperations.Button(locatorType="Xpath", locator=self.ThereXpath).click()              #There .Куда

        day = MainPageLogic.logic().chooseRandomDate()
        ElementOperations.Element(element=day).click()                                              #click on random day

        ElementOperations.Button(locatorType="Xpath", locator=self.FromThereXpath).click()          #Back  .Обратно
        ElementOperations.Button(locatorType="Xpath", locator=self.BackTicketXpath).click()         #dont need backtitle

        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).click()                # click [FROM]
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).send(Keys.BACKSPACE)
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).send(fromC)            #send text [FROM]

        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).click()                  #click [TO]
        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).send(toC)                #send text [TO]
        ElementOperations.Button(locatorType="Xpath", locator=self.DropdownXpath)._find()           #wait for text
        ElementOperations.Button(locatorType="Xpath", locator=self.ConfirmXpath).click()            # CONFIRM



