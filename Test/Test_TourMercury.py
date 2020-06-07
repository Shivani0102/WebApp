import time
import allure
from Mercurytours.Flights import FlightPage
from Mercurytours.Homepage import HomePage
from Mercurytours.Register import RegisterPage
from resources.variables import *
from selenium import webdriver


@allure.title('New user register in this page')
def test_cases(browser):
    global hmpage
    register= RegisterPage(browser)
    hmpage= HomePage(browser)
    register.browser_load()
    hmpage.registerClick()
    register.enterfirstname(firstname)
    register.enterLastname(lastname)
    register.enterPhone(phn)
    register.enterEmail(email)
    register.enterAddress(address)
    register.enterCity(city)
    register.enterState(state)
    register.enterPostal(code)
    register.enterCountry(country)
    register.enterUsername(user)
    register.enterPassword(Pass)
    time.sleep(2)
    register.clickSubmit()
    assert register.matchName()=="Dear "+ firstname+" " +lastname +"," , "line is not matching"
    assert register.usernameMatch() == "Note: Your user name is "+ user+"." , "username is not matching"
    register.Signin()
    register.LoginUser()
    register.LoginPassWord()
    register.LoginSubmitbtn()

@allure.title('Overview of Homepage')
def test_homePage(browser):
    register = RegisterPage(browser)
    hmpage.homeClick()
    time.sleep(2)
    # hmpage.supportClick()
    # hmpage.supportBackClick()
    # time.sleep(2)
    # hmpage.contactClick()
    # hmpage.supportBackClick()
    register.LoginUser()
    register.LoginPassWord()
    register.LoginSubmitbtn()
    verify= hmpage.loginSuccess()
    assert verify== True, "Login not Successfully"
    time.sleep(2)
    hmpage.FlightsClick()
#
# @allure.title('Book flight in this page')
# def test_flightspage(browser):
#     global flight
#     flight = FlightPage(browser)
#     flight.FlightRadio()
#     time.sleep(2)
#     flight.flightDrpDown()
#     flight.flightDeparture()
#     flight.FlightOn()
#     flight.FlightOnday()
#     flight.flightArriving()
#     flight.flightFrom()
#     flight.flightfrmDay()
#     flight.ServiceClass()
#     time.sleep(3)
#     flight.continueClick()
#     flight.backToHome()
#

