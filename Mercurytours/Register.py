import random
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegisterPage:
    URL= "http://demo.guru99.com/test/newtours/"
    registerlink= (By.XPATH,"//a[contains(text(),'REGISTER')]")
    FirstName = (By.XPATH,"//input[@name='firstName']")
    LName = (By.XPATH,"//input[@name='lastName']")
    Phone = (By.XPATH,"//input[@name='phone']")
    Email = (By.XPATH,"//input[@id='userName']")
    Address = (By.XPATH,"//input[@name='address1']")
    City = (By.XPATH,"//input[@name='city']")
    State = (By.XPATH,"//input[@name='state']")
    PostalCode = (By.XPATH,"//input[@name='postalCode']")
    Country = (By.XPATH,"//select[@name='country']")
    Username = (By.XPATH,"//input[@id='email']")
    Password = (By.XPATH,"//input[@name='password']")
    Confirmpass= (By.XPATH,"//input[@name='confirmPassword']")
    submit= (By.XPATH,"//input[@name='submit']")
    match=(By.XPATH,"//img[@src='images/spacer.gif']/parent::td/parent::tr/following-sibling::tr/td[1]/p[1]")
    signin= (By.XPATH,"//a[contains(text(),'sign-in')]")
    usermatch=(By.XPATH,"//img[@src='images/spacer.gif']/parent::td/parent::tr/following-sibling::tr[1]/td[1]/p[3]")
    LoginUsername= (By.XPATH,"//input[@name='userName']")
    LoginPassword= (By.XPATH,"//input[@name='password']")
    LoginSubmit= (By.XPATH,"//input[@name='submit']")

    def __init__(self, driver):
        self.driver= driver

    def browser_load(self):
        self.driver.get(self.URL)

    def registerClick(self):
        self.driver.find_element(*self.registerlink).click()

    def enterfirstname(self,firstname):
        self.driver.find_element(*self.FirstName).send_keys(firstname)

    def enterLastname(self, lastname):
        self.driver.find_element(*self.LName).send_keys(lastname)

    def enterPhone(self,phn):
        self.driver.find_element(*self.Phone).send_keys(phn)

    def enterEmail(self,email):
        self.driver.find_element(*self.Email).send_keys(email)

    def enterAddress(self,address):
        self.driver.find_element(*self.Address).send_keys(address)

    def enterCity(self,city):
        self.driver.find_element(*self.City).send_keys(city)

    def enterState(self,state):
        self.driver.find_element(*self.State).send_keys(state)

    def enterPostal(self,code):
        self.driver.find_element(*self.PostalCode).send_keys(code)

    def enterCountry(self, country):
        randNum = str(random.randrange(1, 25))
        select= Select(self.driver.find_element(*self.Country))
        select.select_by_index(randNum)

    def enterUsername(self,user):
        global text
        self.driver.find_element(*self.Username).send_keys(user)
        text= self.driver.find_element(*self.Username).get_attribute('value')
        print(text)

    def enterPassword(self,Pass):
        global pswrd
        self.driver.find_element(*self.Password).send_keys(Pass)
        time.sleep(2)
        pswrd= self.driver.find_element(*self.Password).get_attribute('value')
        print(pswrd)
        self.driver.find_element(*self.Confirmpass).send_keys(Pass)

    def clickSubmit(self):
        self.driver.find_element(*self.submit).click()

    def matchName(self):
        first_last= self.driver.find_element(*self.match).text
        return first_last

    def usernameMatch(self):
        User = self.driver.find_element(*self.usermatch).text
        return User

    def Signin(self):
        self.driver.find_element(*self.signin).click()

    def LoginUser(self):
        self.driver.find_element(*self.LoginUsername).send_keys(text)

    def LoginPassWord(self):
        self.driver.find_element(*self.LoginPassword).send_keys(pswrd)

    def LoginSubmitbtn(self):
        self.driver.find_element(*self.LoginSubmit).click()




