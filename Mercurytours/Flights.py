import random
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FlightPage:

    """Flights attribute"""
    roundtrip =(By.XPATH ,"//input[@value='roundtrip']")
    oneway =(By.XPATH ,"//input[@value='oneway']")
    flightdrpdown =(By.XPATH ,"//select[@name='passCount']")
    flightdepart =(By.XPATH ,"//select[@name='fromPort']")
    FlightOnmon =(By.XPATH ,"//select[@name='fromMonth']")
    flightsOnday= (By.XPATH,"//select[@name='fromDay']")
    flightarriving= (By.XPATH,"//select[@name='toPort']")
    flightfrmday =(By.XPATH,"//select[@name='toDay']")
    fligthfrm_mon= (By.XPATH,"//select[@name='toMonth']")


    """Prefernces"""
    EconoClass= (By.XPATH,"//input[@value='Coach']")
    businessclass= (By.XPATH,"//input[@value='Business']")
    firstclass= (By.XPATH,"//input[@value='First']")
    airlinedrpdown= (By.XPATH,"//select[@name='airline']")
    continueButton= (By.XPATH,"//input[@name='findFlights']")
    backtohome= (By.XPATH,"//img[@src='images/home.gif']")



    def __init__(self,driver):
        self.driver= driver

    def FlightRadio(self):
        radio1= self.driver.find_element(*self.roundtrip)
        if radio1.is_selected():
            msg=self.driver.find_element(*self.oneway)
            msg.click()
            print('one way is selected')

        else:
            self.driver.find_element(*self.roundtrip).click()
            print('roundtrip is selected')

    def flightDrpDown(self):
        drp=Select(self.driver.find_element(*self.flightdrpdown))
        msg= drp.first_selected_option.text
        print("selected value",msg)
        drp.select_by_visible_text("3")

    def flightDeparture(self):
        drp = Select(self.driver.find_element(*self.flightdepart))
        msg = drp.first_selected_option.text
        print("selected value", msg)
        drp.select_by_visible_text("London")


    def FlightOn(self):
        drp = Select(self.driver.find_element(*self.FlightOnmon))
        msg = drp.first_selected_option.text
        print("selected value", msg)
        drp.select_by_visible_text("February")
        time.sleep(2)

    def FlightOnday(self):
        drp1 = Select(self.driver.find_element(*self.flightsOnday))
        msg1 = drp1.first_selected_option.text
        print("selected value", msg1)
        drp1.select_by_visible_text("18")

    def flightArriving(self):
        drp = Select(self.driver.find_element(*self.flightarriving))
        msg = drp.first_selected_option.text
        print("selected value", msg)
        drp.select_by_visible_text("New York")

    def flightFrom(self):
        drp = Select(self.driver.find_element(*self.fligthfrm_mon))
        msg = drp.first_selected_option.text
        print("selected value", msg)
        drp.select_by_visible_text("June")
        time.sleep(2)


    def flightfrmDay(self):
        drp1 = Select(self.driver.find_element(*self.flightfrmday))
        msg1 = drp1.first_selected_option.text
        print("selected value", msg1)
        drp1.select_by_visible_text("15")

    def ServiceClass(self):
        radio1= self.driver.find_element(*self.EconoClass)
        if radio1.is_selected():
            msg=self.driver.find_element(*self.businessclass)
            if msg.is_selected():
                self.driver.find_element(*self.firstclass).click()
                print('firstclass is selected')
            else:
                msg.click()
            print('businessclass is selected')

        else:
            radio1.click()
            print('service class is selected')


    def continueClick(self):
        self.driver.find_element(*self.continueButton).click()

    def backToHome(self):
        self.driver.find_element(*self.backtohome).click()

