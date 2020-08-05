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
        logger.info("Trying to remvoe booking checkbox")
        ElementOperations.Input(locatorType="Xpath", locator=self.openBookingXpath).click()  # Remove checkbox
        logger.info("Trying to click THERE button")
        ElementOperations.Button(locatorType="Xpath", locator=self.ThereXpath).click()              #There .Куда
        logger.info("Trying to choose a random day")
        day = MainPageLogic.logic().chooseRandomDate()
        logger.info("Trying to click on a random day")
        ElementOperations.Element(element=day).click()                                              #click on random day

        logger.info("Trying to click back button")
        ElementOperations.Button(locatorType="Xpath", locator=self.FromThereXpath).click()          #Back  .Обратно
        logger.info("Trying to click 'Обратный билет не нужен' button")
        ElementOperations.Button(locatorType="Xpath", locator=self.BackTicketXpath).click()         #dont need backtitle

        logger.info("Trying to click FROM button")
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).click()                # click [FROM]
        logger.info("Trying to send BACKSPASE button to input")
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).send(Keys.BACKSPACE)
        logger.info("Trying to send text " + fromC + " to FROM input")
        ElementOperations.Input(locatorType="Xpath", locator=self.FromXpath).send(fromC)            #send text [FROM]

        logger.info("Trying to click TO input")
        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).click()                  #click [TO]
        logger.info("Trying to send text " + toC + " to TO input")
        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).send(toC)                #send text [TO]
        logger.info("Trying to find dropdown")
        ElementOperations.Button(locatorType="Xpath", locator=self.DropdownXpath)._find()           #wait for text
        logger.info("Trying to click TO input")
        ElementOperations.Input(locatorType="Xpath", locator=self.ToXpath).click()  # click [TO]
        logger.info("Trying to click confirm button")
        ElementOperations.Button(locatorType="Xpath", locator=self.ConfirmXpath).click()            # CONFIRM



