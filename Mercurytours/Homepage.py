import random

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    registerlink = (By.XPATH, "//a[contains(text(),'REGISTER')]")
    videoclosebtn= (By.XPATH,"//div[@id='closeBtn']")
    homelink=(By.XPATH,"//a[contains(text(),'Home')]")
    Logo= (By.XPATH,"images/logo.gif")
    signon= (By.XPATH,"//a[contains(text(),'SIGN-ON')]")
    support = (By.XPATH,"//a[contains(text(),'SUPPORT')]")
    contact= (By.XPATH,"//a[contains(text(),'CONTACT')]")
    backtohome= (By.XPATH,"//img[@src='images/home.gif']")
    loginmsg= (By.XPATH,"//h3[contains(text(),'Login Successfully')]")
    Flightlink=(By.XPATH,"//a[contains(text(),'Flights')]")


    def __init__(self, driver):
        self.driver= driver

    def registerClick(self):
        self.driver.find_element(*self.registerlink).click()

    def homeClick(self):
        self.driver.find_element(*self.homelink).click()

    def supportClick(self):
        self.driver.find_element(*self.support).click()

    def supportBackClick(self):
        self.driver.find_element(*self.backtohome).click()

    def contactClick(self):
        self.driver.find_element(*self.contact).click()

    def loginSuccess(self):
        msg= self.driver.find_element(*self.loginmsg).is_displayed()
        return msg

    def FlightsClick(self):
        self.driver.find_element(*self.Flightlink).click()

